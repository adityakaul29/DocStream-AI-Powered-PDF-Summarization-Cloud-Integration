from flask import Flask, request, jsonify, redirect, url_for
import PyPDF2
from transformers import pipeline
import os

# Summarizer setup using Hugging Face's pipeline
summarizer = pipeline("summarization")

# Flask app initialization
app = Flask(__name__)

# Store the summarized result so that it can be accessed via GET request
summary_storage = {}

# Route for PDF upload and summarization
@app.route('/upload', methods=['GET', 'POST'])
def upload_pdf():
    if request.method == 'POST':
        # Check if the request contains a file
        if 'file' not in request.files:
            return jsonify({'error': 'No file uploaded'}), 400
        
        file = request.files['file']
        
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400

        # Read PDF file
        pdf_reader = PyPDF2.PdfReader(file)
        pdf_text = ''

        # Extract text from all pages of the PDF
        for page_num in range(len(pdf_reader.pages)):
            pdf_text += pdf_reader.pages[page_num].extract_text()

        # Summarize the text using the transformer pipeline
        summary = summarizer(pdf_text, max_length=150, min_length=30, do_sample=False)
        summary_text = summary[0]['summary_text']

        # Store the summary for later retrieval via GET request
        summary_storage['summary'] = summary_text
        
        return jsonify({'message': 'PDF successfully summarized', 'summary': summary_text})

    # If GET request, render a basic upload form
    return '''
    <!doctype html>
    <title>Upload PDF for Summarization</title>
    <h1>Upload PDF for Summarization</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

# Route to get the summarized PDF text as JSON
@app.route('/summary', methods=['GET'])
def get_summary():
    # Return the stored summary as a JSON response
    if 'summary' in summary_storage:
        return jsonify({'summary': summary_storage['summary']})
    else:
        return jsonify({'error': 'No summary found. Upload a PDF first.'}), 404

if __name__ == '__main__':
    app.run(port=5000)
