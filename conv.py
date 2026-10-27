
from pdf2image import convert_from_path
from pathlib import Path

# Input PDF file
pdf_path = "eileen pesapal scan.pdf"

# Folder to save the JPG images
output_folder = Path("output_images")
output_folder.mkdir(parents=True, exist_ok=True)

pages = convert_from_path(
    pdf_path,
    dpi=200,
    fmt="jpeg",
    poppler_path=r"C:\Users\ICT\Downloads\Release-26.09.0-0\poppler-26.09.0\Library\bin"
)

# Save each page as a numbered JPG
for page_number, page in enumerate(pages, start=1):
    output_path = output_folder / f"{page_number}.jpg"
    page.save(output_path, "JPEG", quality=95)
    print(f"Saved: {output_path}")

print("PDF conversion completed!")
