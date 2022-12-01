# Install pyQRCode and pypng using pip
import pyqrcode
import png
link = "https://www.instagram.com/_dracu.la_/"
qr_code = pyqrcode.create(link)
qr_code.png("instagram.png", scale=5)