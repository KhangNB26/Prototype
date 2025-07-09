import os
from paddleocr import PaddleOCR
from jiwer import wer
import pandas as pd
from sklearn.metrics import precision_score, recall_score

# ----- Configuration -----
datasets = [
    {
    "name": "English",
    "image_dir": "Prototype/English_Image",
    "ground_truth_csv": "Prototype\English_Image\English_GroundTruth.csv",
    "lang": "en",
    },
    {
    "name": "French",
    "image_dir": "Prototype/French_Image",
    "ground_truth_csv": "Prototype\French_Image\French_GroundTruth.csv",
    "lang": "fr",
    }
]

# Create lists to store results
all_results = []
all_y_true = []
all_y_pred = []

# ----- Processing Datasets -----
for dataset in datasets:
    print(f"\n--- Evaluating {dataset['name']} Dataset ---")
    
    # Initialize PaddleOCR for the language
    ocr_model = PaddleOCR(use_textline_orientation=True, lang=dataset["lang"])
    
    # Load ground truth CSV
    gt_df = pd.read_csv(dataset["ground_truth_csv"])
    gt_df.set_index("Image", inplace=True)
    
    # Lists to store results for this dataset
    dataset_results = []
    dataset_y_true = []
    dataset_y_pred = []
    
    # Process images
    for img_file in sorted(os.listdir(dataset["image_dir"])):
        if not img_file.lower().endswith((".jpg", ".png", ".jpeg")):
            continue  # Skip non-image files
        
        img_path = os.path.join(dataset["image_dir"], img_file)
        ocr_result = ocr_model.predict(img_path)
        print(ocr_result)
        
        # Extract text from OCR result  
        if isinstance(ocr_result, list) and len(ocr_result) > 0:
            rec_texts = ocr_result[0].get('rec_texts', [])
            extracted_text = " ".join(rec_texts).strip()
        else:
            extracted_text = ""

        # Get ground truth text
        # Remove file extension for matching
        img_file = os.path.splitext(img_file)[0]  # Remove extension for matching
        if img_file in gt_df.index:
            true_text = str(gt_df.loc[img_file, "Ground Truth Label"]).strip()
        else:
            true_text = ""

        # Add to results
        dataset_y_true.append(true_text)
        dataset_y_pred.append(extracted_text)

        # Append results
        dataset_results.append({
            "dataset": dataset["name"],
            "filename": img_file,
            "ground_truth": true_text.strip(),
            "predicted_text": extracted_text,
            "exact_match": int(true_text.strip() == extracted_text),
            "wer": wer([true_text.strip()], [extracted_text])  # WER per image
        })
    # ----- Dataset Metrics -----
    # Convert Ground Truth and Predicted Text to characters
    y_true_chars = "".join(dataset_y_true)
    y_pred_chars = "".join(dataset_y_pred)

    # Create vectors for precision and recall
    min_len = min(len(y_true_chars), len(y_pred_chars))
    y_true_vec = [1] * min_len
    y_pred_vec = [int(y_true_chars[i] == y_pred_chars[i]) for i in range(min_len)]

    # Calculate precision and recall, based on each character
    precision = precision_score(y_true_vec, y_pred_vec)
    recall = recall_score(y_true_vec, y_pred_vec)

    print(f"Precision: {precision:.4f}")
    print(f"Recall:    {recall:.4f}")

    # Append dataset results to global results
    all_results.extend(dataset_results)
    all_y_true.extend(dataset_y_true)
    all_y_pred.extend(dataset_y_pred)


# --- EXPORT RESULTS TO CSV ---
results_df = pd.DataFrame(all_results)
results_df.to_csv("Prototype\ocr_evaluation_all.csv", index=False, encoding="utf-8-sig")
print("Combined evaluation exported to ocr_evaluation_all.csv")