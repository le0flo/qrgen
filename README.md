# QRCode generator

### Requirements

- [Python >= 3.13](https://www.python.org/)

### Installation

1. Create a python virtual environment with `python -m venv venv`
2. Enter the environment using `source venv/bin/activate`
3. Run `pip install -r requirements.txt`

### Usage

- Generate a normal qrcode: `python main.py [content] [out.png]`
- Generate a qrcode with a centered logo: `python main.py [content] [out.png] [logo.png]`
