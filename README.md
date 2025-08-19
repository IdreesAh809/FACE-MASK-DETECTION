# FACE-MASK-DETECTIO# Face Mask Detection

[Live Demo](https://face-mask-detection-ongdh3wsxcarc75sv6xgs2.streamlit.app/)

A web application built with Streamlit that uses a pre-trained deep learning model to detect whether a person is wearing a face mask.

## Features

- Detects Mask / No Mask in uploaded images.
- Shows confidence percentage.
- Easy-to-use web interface via Streamlit.

## Installation

1. Clone the repository and navigate into it:

```bash
git clone https://github.com/IdreesAh809/FACE-MASK-DETECTION.git
cd FACE-MASK-DETECTION
```

2. **Create and activate a virtual environment:**
```bash
python -m venv venv
.\venv\Scripts\activate   # Windows
source venv/bin/activate  # Mac/Linux
```
3. **Install dependencies and run the app:**
```bash
pip install -r requirements.txt
streamlit run app/streamlit_app.py
```
## Usage
1. **Upload an image of a person.**
2. **The app will predict whether the person is wearing a mask or not and display the confidence percentage.**

## License
This project is open-source and free to use.