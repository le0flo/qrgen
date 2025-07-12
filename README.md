# QR code generator

### Requirements

- [Python >= 3.13](https://www.python.org/)

### Installation

1. Create a python virtual environment with `python -m venv venv`
2. Enter the environment using `source venv/bin/activate`
3. Install the required packages by executing `pip install -r requirements.txt`

### Usage

```sh
cd qrgen
python main.py https://example.com out.png # Generates a qrcode that encodes 'https://example.com'
```
