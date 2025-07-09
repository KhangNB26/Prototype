# Hekate Prototype

Welcome to the **Hekate Prototype**! This folder contains the initial implementation and experimental features for the Hekate project.

## Structure

- `English_Image` — Image contains texts in English for OCR.
- `French_Image` — Image contains texts in French for OCR.
- `ocr_evaluation.py` — Code for evaluating ocr.
- `ocr_extract_json.py` — Process of: Load image -> OCR -> Extract text in JSON

## Getting Started

1. Clone the repository:
    ```bash
    git clone https://github.com/KhangNB26/Prototype.git
    cd Prototype
    ```
2. Install Dependencies
    ```bash
    pip install scikit-learn paddlepaddle paddleocr jiwer pandas
    ```
3. OCR Evaluation
    To evaluate the OCR using PaddleOCR, run the provided scripts:
    ```bash
    python Prototype/ocr_evaluation.py
    ```
    This will result a csv file called ocr_evaluation_all.csv. Open this file to see:
    - Ground Truth - True text of image
    - Predict Text - Text extracted by OCR
    - Exact Match - Return 1 if two sentence are the same, 0 in contrast
    - wer - Word Error
    Metrics used for evaluating are Precision/Recall: Calculate for each character
4. OCR Scripts
    To see the simple demo of process: Load image -> OCR -> Output text in JSON, run the provided scripts:
    ```bash
    python Prototype/ocr_extract_json.py
    ```
    Output is a json file contains:
    - image_path - Path of the image
    - ocr_result - Include:
        - text - Extracted text
        - confidence
        - bounding box

Note: English Image works well, but I'm using French Image in 1800s so the results might be not that correct.