# OCR Tool 🔍

A command-line OCR tool that extracts text from images and saves it to a text file, with support for both English and Arabic.

## Features
- Extracts text from images using EasyOCR
- Supports English and Arabic text
- Saves extracted text to a .txt file automatically
- Handles file path errors gracefully

## How to Use
Run the script:

python ocr_tool.py

Then follow the prompt:

Please enter image path: C:/Users/YourName/Pictures/scan.png

The extracted text will print to the console and be saved to image_text.txt in the same folder.

## Output
A file called image_text.txt will be created containing all detected text, for example:

Invoice #1234
Total: 500.00

## Supported Image Formats
- PNG
- JPG / JPEG
- BMP
- TIFF

## Requirements
- Python 3.x
- easyocr

## Installation
pip install easyocr

## Notes
- First run will download the EasyOCR language models automatically
- For best results use clear, high resolution images
