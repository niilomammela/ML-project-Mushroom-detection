import os
from PIL import Image


input_folder = "Arkisto/merged_dataset"


output_folder = "dataset_resized"
os.makedirs(output_folder, exist_ok=True)


target_size = (224, 224)


for root, _, files in os.walk(input_folder):
    for file in files:
        if file.lower().endswith((".png", ".jpg", ".jpeg")):
            input_path = os.path.join(root, file)

            relative_path = os.path.relpath(root, input_folder)
            output_dir = os.path.join(output_folder, relative_path)
            os.makedirs(output_dir, exist_ok=True)

            output_path = os.path.join(output_dir, file)

            try:
                img = Image.open(input_path)

                img = img.convert("RGB")

                img = img.resize(target_size, Image.LANCZOS)

                img.save(output_path, "JPEG", quality=90)

            except Exception as e:
                print(f"Could not process {input_path}: {e}")

print("Resizing complete! All resized images saved in:", output_folder)
