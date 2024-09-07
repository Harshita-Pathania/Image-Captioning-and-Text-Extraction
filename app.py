import streamlit as st
import openai
import pytesseract
from PIL import Image
import random

# Set up OpenAI API credentials
openai.api_key = ""

# Define a function to generate image captions
def generate_caption(image):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Generate a concise caption for the image:\n{image}"}
        ],
        temperature=0.5
    )
    return response.choices[0].message.content.strip()




# Define a function to extract text from an image
import subprocess

def extract_text_from_image(image):
    image_path = "temp_image.png"
    image.save(image_path)

    result = subprocess.run(['tesseract', image_path, 'stdout'], capture_output=True, text=True)
    if result.returncode == 0:
        extracted_text = result.stdout.strip()
        return extracted_text
    else:
        return None



# Create the Streamlit app
def main():
    st.title("Image Captioning and Text Extraction Web App")
    st.write("Upload an image and choose the action to perform.")

    # User input
    image = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])

    # Buttons to trigger actions
    caption_button = st.button("Generate Caption")
    extract_button = st.button("Extract Text")

    if caption_button and image is not None:
        # Generate caption
        caption = generate_caption(image)
        st.text("Caption:")
        st.write(caption)

        # Display the uploaded image
        st.text("Uploaded Image:")
        st.image(image, use_column_width=True)

    if extract_button and image is not None:
        # Extract text from the image
        pil_image = Image.open(image)
        extracted_text = extract_text_from_image(pil_image)
        st.text("Extracted Text:")
        st.write(extracted_text)

        # Display the uploaded image
        st.text("Uploaded Image:")
        st.image(image, use_column_width=True)

# Run the app
if __name__ == "__main__":
    main()
