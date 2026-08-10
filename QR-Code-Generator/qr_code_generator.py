import qrcode

# Generate QR Code
def generate_qr(text):
    if text == "":
        print("Please enter some text or link.")
        return

    qr = qrcode.make(text)
    qr.save("my_qr_code.png")

    print("QR Code generated successfully!")
    print("Saved as my_qr_code.png")


# Main program
text = input("Enter Text or URL: ")

generate_qr(text)
