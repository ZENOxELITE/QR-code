
import streamlit as st
import qrcode
from PIL import Image
import io

st.title("Welcome to QR Code Generator")

ask = st.text_input("Enter the link")

if st.button("Generate QR Code"):

    # Create QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=3,
    )

    qr.add_data(ask.strip())
    qr.make(fit=True)

    img = qr.make_image(fill_color="white", back_color="black")

    # Convert PIL image to bytes
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    byte_img = buf.getvalue()

    st.success("QR Code created successfully!")

    # Show QR on screen
    st.image(byte_img, caption="Generated QR Code")

    # Download button
    st.download_button(
        label="Download QR Code",
        data=byte_img,
        file_name="qrcode.png",
        mime="image/png"
    )

