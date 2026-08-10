from PIL import Image

images = []

# Enter image paths
while True:
    path = input("Enter image path (done to finish): ")

    if path.lower() == "done":
        break

    image = Image.open(path)
    images.append(image)

# Convert images to RGB
for i in range(len(images)):
    images[i] = images[i].convert("RGB")

# PDF name
pdf_name = input("Enter PDF name: ")

if not pdf_name.endswith(".pdf"):
    pdf_name += ".pdf"

# Create PDF
images[0].save(
    pdf_name,
    save_all=True,
    append_images=images[1:]
)

print("PDF created:", pdf_name)
