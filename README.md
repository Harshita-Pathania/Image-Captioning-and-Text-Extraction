# Image Captioning and Text Extraction Web App

## Overview
This web application allows users to upload an image and either generate a concise caption or extract text from the image using OCR. The app is built using **Streamlit** and utilizes **OpenAI's GPT-3.5 Turbo** for caption generation and **Tesseract OCR** for text extraction.

## Features
1. **Generate Captions**: Automatically generate a concise caption for an uploaded image using GPT-3.5 Turbo.
2. **Extract Text from Images**: Extract text from an uploaded image using Tesseract OCR.
3. **Display Image**: Uploaded images are displayed within the app.

## Requirements
- Python 3.x
- Streamlit
- OpenAI API key
- Tesseract OCR

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
   ```

2. Install the required Python packages:
   ```bash
   pip install streamlit openai pytesseract pillow
   ```

3. Install **Tesseract OCR**:
   - On Ubuntu:
     ```bash
     sudo apt-get install tesseract-ocr
     ```
   - On macOS (via Homebrew):
     ```bash
     brew install tesseract
     ```
   - On Windows: [Download and install Tesseract OCR](https://github.com/tesseract-ocr/tesseract/wiki)

4. Set up your OpenAI API key:
   Replace the placeholder `sk-...` in the script with your OpenAI API key.

## How to Use

1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Upload an image in **PNG**, **JPG**, or **JPEG** format.

3. Choose an action:
   - **Generate Caption**: Click the "Generate Caption" button to receive a caption for the uploaded image.
   - **Extract Text**: Click the "Extract Text" button to retrieve any text found in the image.

4. The app will display the caption or extracted text along with the uploaded image.

## Example
After uploading an image, the app will:
- Display the image.
- Either generate a caption or extract and display any text found within the image.
