# File: convert.py
import os
from pdf2docx import Converter

# Folders
INPUT_DIR = "input"
OUTPUT_DIR = "output"

# Ensure folders exist
os.makedirs(INPUT_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Get all PDFs in input folder
pdf_files = [f for f in os.listdir(INPUT_DIR) if f.lower().endswith(".pdf")]

if not pdf_files:
    print("⚠️ No PDFs found in input/. Nothing to convert.")
    exit(0)  # prevents exit code 2

for filename in pdf_files:
    pdf_path = os.path.join(INPUT_DIR, filename)
    docx_name = os.path.splitext(filename)[0] + ".docx"
    docx_path = os.path.join(OUTPUT_DIR, docx_name)

    try:
        print(f"Converting {pdf_path} → {docx_path}")
        cv = Converter(pdf_path)
        cv.convert(docx_path, start=0, end=None)
        cv.close()
        print(f"✅ Saved {docx_path}")
    except Exception as e:
        print(f"❌ Failed to convert {filename}: {e}")
