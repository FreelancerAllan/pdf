from PIL import Image
from pathlib import Path

# Folder containing the JPG images
input_folder = Path("output_images")

# Output PDF file
output_pdf = "combined.pdf"

# Get all JPG images in numerical order
image_files = sorted(
    input_folder.glob("*.jpg"),
    key=lambda x: int(x.stem)
)

if not image_files:
    print("No JPG images found!")
    exit()

# Open and convert images to RGB
images = []

for image_file in image_files:
    img = Image.open(image_file).convert("RGB")
    images.append(img)

# Save all images into one PDF
images[0].save(
    output_pdf,
    save_all=True,
    append_images=images[1:],
    resolution=200
)

# Close images
for img in images:
    img.close()

print(f"PDF created successfully: {output_pdf}")