import cv2
import os
from tqdm import tqdm


TARGET_SIZE = (640, 640) 


DATA_DIR = "./data/train/" 


all_files = os.listdir(DATA_DIR)
image_files = [f for f in all_files if '_mask' not in f and f.endswith(('.jpg', '.png', '.jpeg'))]

print(f"Found {len(image_files)} images to process in {DATA_DIR}...")

for img_name in tqdm(image_files):
    
    img_path = os.path.join(DATA_DIR, img_name)
    
    base_name, _ = os.path.splitext(img_name)
    mask_name = f"{base_name}_mask.png" 
    mask_path = os.path.join(DATA_DIR, mask_name)

    try:
        # Read image and mask
        image = cv2.imread(img_path)
        mask = cv2.imread(mask_path)
        
        
        if image is None:
            print(f"Warning: Could not read image file {img_path}. Skipping.")
            continue
        if mask is None:
            print(f"Warning: Could not find or read mask file {mask_path}. Skipping.")
            continue

  
        image_resized = cv2.resize(image, TARGET_SIZE, interpolation=cv2.INTER_AREA)
        mask_resized = cv2.resize(mask, TARGET_SIZE, interpolation=cv2.INTER_NEAREST)
        
        
        cv2.imwrite(img_path, image_resized)
        cv2.imwrite(mask_path, mask_resized)

    except Exception as e:
        print(f"An unexpected error occurred while processing {img_name}: {e}")

print("\nPreprocessing complete.")