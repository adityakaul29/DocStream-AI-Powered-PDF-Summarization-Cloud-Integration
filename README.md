# DocStream: AI-Powered PDF Summarization & Cloud Integration

## Overview

**DocStream** is a Python-based tool that automates the process of summarizing PDF documents and sharing them via Google Drive. This tool is ideal for anyone who regularly works with large PDF files and needs to generate concise summaries for quick review. The summarized documents are automatically uploaded to a designated folder in Google Drive, and a shareable link is generated for easy access.

## Features

- **Automatic PDF Upload**: Upload your PDF file directly in Google Colab.
- **AI-Powered Summarization**: Utilizes advanced NLP models to generate concise and accurate summaries of the uploaded PDF.
- **Google Drive Integration**: Automatically uploads the summarized PDF to a specified folder ("DoShare") in your Google Drive.
- **Shareable Link Generation**: Generates a shareable link for easy distribution of the summarized document.

## How It Works

1. **File Upload**: Users upload a PDF file directly in Google Colab.
2. **Text Extraction**: The content of the PDF is extracted using the `PyMuPDF` library.
3. **Summarization**: The extracted text is summarized using the `facebook/bart-large-cnn` model from the `transformers` library.
4. **Google Drive Upload**: The summarized PDF is automatically uploaded to a folder named "DoShare" in your Google Drive.
5. **Link Generation**: A shareable link to the uploaded file is generated and printed in the Colab notebook.

## Setup and Installation

### Prerequisites

- Python 3.7 or higher
- Google Colab environment
- Google Drive account

### Installation

Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/docstream.git
