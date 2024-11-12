import time
# Start measuring time
start_time = time.time()

import os
import pandas as pd
import requests
from PIL import Image
from io import BytesIO

def download_image(url, idx):
    image_path = os.path.join(IMAGE_DIR, f"{idx}.jpg")
    if not os.path.exists(image_path):
        try:
            response = requests.get(url)
            img = Image.open(BytesIO(response.content))
            img.save(image_path)
            print(f"Downloading Image: {idx}")
        except Exception as e:
            print(f"Error downloading Image: {idx}")
            black_image = Image.new('RGB', IMG_SIZE, color=(0, 0, 0))
            black_image.save(image_path)
        finally:
            return image_path
    print(f"Image Is Already Downloaded: {idx}")
    return image_path

if __name__ == "__main__":
    IMAGE_DIR='image_test/'
    if not os.path.exists(IMAGE_DIR):
        os.makedirs(IMAGE_DIR)
    IMG_SIZE = (128, 128)  # Must match the input size of your trained model
    Start_point = 0
    end_point = 100
    
    df = pd.read_csv(os.path.join('dataset/', 'test.csv')).iloc[Start_point:end_point]
    for idx, row in df.iterrows():
        try:
            path = download_image(row['image_link'], idx)
        except Exception as e:
            print(f"Error In Processing Image {idx}")

# End measuring time
end_time = time.time()

# Calculate the time taken
time_taken = end_time - start_time

# Print the time taken
print(f"Time taken to download images: {time_taken:.2f} seconds")
