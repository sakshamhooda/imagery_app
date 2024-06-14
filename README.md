# imagery_app

This FastAPI application leverages Tesseract OCR to provide Optical Character Recognition (OCR) services. It offers two primary functionalities: extracting plain text from images and retrieving bounding boxes around text elements like words, lines, paragraphs, and blocks. This service can be useful for applications that need to digitize documents and perform text analysis or automated data extraction.

## Features

- **Text Extraction**: Convert images containing typed or handwritten text into plain text.
- **Bounding Box Retrieval**: Get coordinates of text elements based on the desired granularity (word, line, paragraph, block).

## Prerequisites

- Python 3.9+
- FastAPI
- Uvicorn
- Pytesseract
- Pillow
- Tesseract OCR

## Installation

First, ensure that Python and Tesseract OCR are installed on your machine. Tesseract OCR can be downloaded from [here](https://github.com/tesseract-ocr/tesseract).

### Install Python Dependencies

Run the following command to install the required Python libraries:

```bash
pip install fastapi uvicorn pytesseract Pillow
