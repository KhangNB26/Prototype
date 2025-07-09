import os
from paddleocr import PaddleOCR
import json
from PIL import Image

# ----- CONFIGURATION -----
image_dir = "Prototype\English_Image"
output_json = "Prototype\ocr_output.json"
language = "en"  # Change to "fr" for French

# ----- OCR INITIALIZATION -----
ocr_model = PaddleOCR(use_textline_orientation=True, lang=language)

# Function to process image and extract text
def process_images(image_path):
    ocr_result = ocr_model.predict(image_path)
    # Extract text from OCR result
    if isinstance(ocr_result, list) and len(ocr_result) > 0:
        res = ocr_result[0]  # Assuming the first element contains the OCR results
        ocr_data = []
        for text, score, poly in zip(res['rec_texts'], res['rec_scores'], res['dt_polys']):
            ocr_data.append({
                "text": text,
                "confidence": score,
                "bounding_box": poly.tolist()  # numpy array -> list
            })
        return {
            "image_path": image_path,
            "ocr_result": ocr_data
        }
    else:
        return {
            "image_path": image_path,
            "ocr_result": []
        }
    
# ----- MAIN WORKFLOW -----
def main():
    results = []
    for img_file in sorted(os.listdir(image_dir)):
        if not img_file.lower().endswith((".jpg", ".png", ".jpeg")):
            continue  # Skip non-image files
        
        img_path = os.path.join(image_dir, img_file)
        print(f"Processing {img_path}...")
        result = process_images(img_path)
        results.append(result)
    
    # Save results to JSON file
    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)
    print(f"Results saved to {output_json}")

if __name__ == "__main__":
    main()