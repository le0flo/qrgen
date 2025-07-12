# QR code generator

### Requirements

- [Python >= 3.13](https://www.python.org/)

### Usage

```sh
git clone https://github.com/le0flo/qrgen.git
cd qrgen
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py https://example.com out.png # Generates a qrcode that encodes 'https://example.com'
```
