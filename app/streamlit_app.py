# app/streamlit_app.py

import streamlit as st
import cv2
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image
import os

# Load model
MODEL_PATH = "model/face_mask_model.h5"
model = load_model(MODEL_PATH)

# Preprocess function (moved here from utils.py)
def prepare_image(image, target_size=(128, 128)):
    image = image.convert("RGB")  # Ensure 3 channels
    image = np.array(image)
    image = cv2.resize(image, target_size)  # Resize to 128x128
    image = image / 255.0  # Normalize
    image = np.expand_dims(image, axis=0)  # Add batch dimension -> (1,128,128,3)
    return image


# Prediction
def predict_mask(image):
    processed_image = prepare_image(image, target_size=(128, 128))
    prediction = model.predict(processed_image)[0]  # e.g., [0.9, 0.1]

    # Get class label
    class_index = int(np.argmax(prediction))   # force int
    confidence = float(np.max(prediction) * 100)  # force Python float

    label = "Mask" if class_index == 0 else "No Mask"
    return label, confidence

# Streamlit UI
st.title("😷 Face Mask Detection")
st.write("Upload an image to check if the person is wearing a mask or not.")

uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    label, confidence = predict_mask(image)
    st.subheader(f"Prediction: {label}")
    st.write(f"Confidence: {confidence:.2f}%")

st.markdown("---")
