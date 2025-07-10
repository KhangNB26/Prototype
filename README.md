# Hekate Prototype

Welcome to the **Hekate Prototype**! This folder contains the initial implementation and experimental features for the Hekate project.

---

## 📁 Project Structure

- **English_Image/** — Images with English text for OCR evaluation.
- **French_Image/** — Images with French text for OCR evaluation.
- **ocr_evaluation.py** — Script for evaluating OCR performance.
- **ocr_extract_json.py** — Script for extracting OCR results and exporting them as JSON.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/KhangNB26/Prototype.git
cd Prototype
```

### 2. Install Dependencies

```bash
pip install scikit-learn paddlepaddle paddleocr jiwer pandas
```

---

## 📝 Usage

### 1. OCR Evaluation

Run the evaluation script to assess OCR performance:

```bash
python Prototype/ocr_evaluation.py
```

This will generate a CSV file named `ocr_evaluation_all.csv` containing:

- **Ground Truth** — True text from the image
- **Predict Text** — Text extracted by OCR
- **Exact Match** — 1 if prediction matches ground truth, 0 otherwise
- **WER** — Word Error Rate
- **Precision/Recall** — Calculated per character

---

### 2. OCR Extraction to JSON

Run the extraction script for a demo of the process (Load image → OCR → Output JSON):

```bash
python Prototype/ocr_extract_json.py
```

This will output a JSON file with:

- `image_path` — Path to the processed image
- `ocr_result`:
    - `text` — Extracted text
    - `confidence` — OCR confidence score
    - `bounding box` — Location of detected text

---

## ⚠️ Notes

- The OCR works well on English images.
- Results on French images (especially from the 1800s) may be less accurate due to historical font and