# imagery_app

This FastAPI application leverages Tesseract OCR to provide Optical Character Recognition (OCR) services. It offers two primary functionalities: extracting plain text from images and retrieving bounding boxes around text elements like words, lines, paragraphs, and blocks. This service can be useful for applications that need to digitize documents and perform text analysis or automated data extraction.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
  - [Install Python Dependencies](#install-python-dependencies)
- [Application run and API testing](#application-run-and-api-testing)
  - [Run the app server](#run-the-app-server)
  - [Run the tests](#run-the-tests)
- [Endpoint verification](#endpoint-verification)
  - [Extract text](#extract-text)
  - [Extract Bounding Box](#extract-bounding-box)
- [Docker Image](#docker-image)
  - [Build the docker image](#build-the-docker-image)
  - [Run the docker container](#run-the-docker-container)
- [License](#license)

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

```
## Application run and API testing
The tests have been cloned from [here] (https://github.com/AbhilakshSinghReen/tesseract-ocr-assignment-api-tester). 
You may follow the instructions as it is on the given repo or simply put it into your tests folder.

Run the app server using either of following commands :

```bash 
uvicorn main:app --host 0.0.0.0 --port 8000
```

or

```bash
python main.app
```

If you are putting tests from the repo to your folder as in this repository, in a sepeare terminal run following command
```bash
pytest
```

## Endpoint verification 

You can use tools like curl, Postman, or any API testing tool to verify the endpoints.

Extract text

```sh
curl -X POST "http://localhost:8000/api/get-text" -H "Content-Type: application/json" -d "{\"base64_image\": \"<your_base64_encoded_image>\"}"
```

Extraxt Bounding Box

```sh
curl -X POST "http://localhost:8000/api/get-bboxes" -H "Content-Type: application/json" -d "{\"base64_image\": \"<your_base64_encoded_image>\", \"bbox_type\": \"word\"}"
```

## Docker Image

1. Build the docker image.
```bash 
docker build -t tesseract-ocr-api .
```

2. Run the docker container.
```bash
docker build -t tesseract-ocr-api .
```

## License
This project is under MIT license.