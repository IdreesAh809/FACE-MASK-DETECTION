# Face Mask Detection

[**Live Demo**](https://face-mask-detection-ongdh3wsxcarc75sv6xgs2.streamlit.app/)

A web application built with Streamlit that uses a trained deep learning model to identify whether a person is wearing a face mask

## Features
- Detects **Mask / No Mask** in uploaded images.
- Shows **confidence percentage**.
- Easy-to-use web interface via Streamlit.

## Installation
1. Clone the repo:
git clone https://github.com/IdreesAh809/FACE-MASK-DETECTION.git
cd FACE-MASK-DETECTION

2. Create a virtual environment and activate it:
python -m venv venv
.\venv\Scripts\activate   # Windows
source venv/bin/activate  # Mac/Linux

3. Install dependencies:
pip install -r requirements.txt

4. Run the app:
streamlit run app/streamlit_app.py

## Usage
- Upload an image of a person.  
- The app will predict whether the person is wearing a mask or not and display the confidence percentage.  

## License
This project is open-source and free to use.
