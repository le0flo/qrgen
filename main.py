import sys
import qrcode
from PIL import Image

# QRCode Settings
qr = qrcode.QRCode(
    version=5,
    box_size=50,
    border=4,
)

if len(sys.argv) >= 3:
    content = sys.argv[1]
    output = sys.argv[2]

    qr.add_data(content)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output)

    if len(sys.argv) == 4:
        qr_code = Image.open(output).convert('RGB')
        qr_w, qr_h = qr_code.size

        logo = sys.argv[3]
        logo = Image.open(logo).convert('RGB')
        logo = logo.resize((int(qr_w/4), int(qr_h/4)))
        logo_w, logo_h = logo.size

        paste_w = int(qr_w/2 - (logo_w/2))
        paste_h = int(qr_h/2 - (logo_h/2))

        qr_code.paste(logo, (paste_w, paste_h))
        qr_code.save(output)
    elif len(sys.argv) > 4:
        print("Too many arguments! Aborting.")
else:
    print("Invalid arguments! Aborting.")
