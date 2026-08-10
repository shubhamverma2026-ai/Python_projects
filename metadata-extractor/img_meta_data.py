from PIL import Image, ExifTags
import os

path = input("Enter image path: ")

image = Image.open(path)

print("\nIMAGE INFORMATION")
print("----------------------")
print("File Name:", os.path.basename(path))
print("File Type:", image.format)
print("File Size:", round(os.path.getsize(path) / 1024, 2), "KB")
print("Width:", image.width, "pixels")
print("Height:", image.height, "pixels")

print("\nEXIF METADATA")
print("----------------------")

exif = image.getexif()

if not exif:
    print("No EXIF metadata found.")
else:
    for tag, value in exif.items():
        name = ExifTags.TAGS.get(tag, tag)
        print(name, ":", value)

# Save report
with open("metadata_report.txt", "w") as file:
    file.write("IMAGE METADATA\n\n")

    for tag, value in exif.items():
        name = ExifTags.TAGS.get(tag, tag)
        file.write(f"{name}: {value}\n")

print("\nReport saved as metadata_report.txt")
