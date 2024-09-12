# DocStream: AI-Powered PDF Summarization & Cloud Integration

**DocStream** is an AI-powered web service that allows users to summarize PDF documents using a GET request. The service uses a pre-trained BART model from Hugging Face's `transformers` library to generate concise summaries. It also exposes the API to the internet via ngrok, enabling access from anywhere.

## Features
- Summarize PDFs by sending a base64-encoded string through a GET request.
- AI-powered text summarization using the **facebook/bart-large-cnn** model.
- Exposes the Flask server publicly using **ngrok**.

## Technologies Used
- **Flask**: Python web framework for building the API.
- **ngrok**: Tool to expose the Flask app to the public internet.
- **Hugging Face Transformers**: Provides pre-trained NLP models for text summarization.
- **PyMuPDF (fitz)**: Extracts text from PDF files.

## How it Works

1. **Upload PDF**: The client sends a base64-encoded PDF string as a query parameter.
2. **Extract Text**: The server decodes the PDF and extracts its text.
3. **Summarize Text**: The extracted text is summarized using the `facebook/bart-large-cnn` model.
4. **Response**: The summarized text is returned in the JSON response.

## Installation and Setup

### Step 1: Clone the Repository
``bash
git clone https://github.com/yourusername/docstream.git
cd docstream

Step 2: Install the Required Dependencies
Make sure you have Python installed, then install the necessary packages:

pip install flask flask-ngrok transformers PyMuPDF

Step 3: Run the Application
Start the Flask app with ngrok:
python app.py


Once the app is running, ngrok will provide you with a public URL (e.g., http://xyz123.ngrok.io). This URL can be used to interact with the API from anywhere.

API Usage
1. Endpoint: /summarize-pdf
Method: GET
URL: http://<ngrok-url>/summarize-pdf
Query Parameter:
pdf: The base64-encoded PDF file content.
Example Request
Use Postman or curl to make a request:

curl "http://<ngrok-url>/summarize-pdf?pdf=BASE64_ENCODED_PDF"

{
  "summary": "This is the summarized content of your PDF..."
}

Testing with Postman
Open Postman.
Set the method to GET.
Set the URL to the ngrok URL with /summarize-pdf.
Add the pdf query parameter with the base64-encoded PDF string.
Hit Send and receive the summarized text in the response.
License
This project is licensed under the MIT License.


This is a complete **README** in markdown format that can be copied and pasted directly into your project. Let me know if you need any further assistance!

