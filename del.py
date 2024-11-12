import os

def delete_image(image_path):
  if os.path.exists(image_path):
    os.remove(image_path)

for i in range(44009,89365):
  image_path = os.path.join('test_cases/', f"{i}.jpg")
  delete_image(image_path)
