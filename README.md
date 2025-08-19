# Face Mask Detection

[Live Demo](https://face-mask-detection-ongdh3wsxcarc75sv6xgs2.streamlit.app/)

A web application built with Streamlit that uses a trained deep learning model to identify whether a person is wearing a face mask.

## Features

- Detects Mask / No Mask in uploaded images.
- Shows confidence percentage.
- Easy-to-use web interface via Streamlit.

## Project Structure
```
FACE-MASK-DETECTION
├── app
│   ├── __pycache__
│   ├── streamlit_app.py
│   └── utils.py
├── mask-detection-data
│   ├── with_mask
│   └── without_mask
├── model
│   └── face_mask_model.h5
├── notebook
│   └── face-mask-detect.ipynb
├── venv
└── run.py
```


## Installation

1. **Clone the repository and navigate into it:**

```bash
git clone https://github.com/IdreesAh809/FACE-MASK-DETECTION.git
cd FACE-MASK-DETECTION
```
2. **Create and activate a virtual environment:**
```
python -m venv venv
.\venv\Scripts\activate   # Windows
source venv/bin/activate  # Mac/Linux
```
4. **Install dependencies and run the app:**
```
pip install -r requirements.txt
streamlit run app/streamlit_app.py
```
## Usage

1. **Upload an image of a person:**
2. **The app will predict whether the person is wearing a mask or not and display the confidence percentage:**

## License
**This project is open-source and free to use**

