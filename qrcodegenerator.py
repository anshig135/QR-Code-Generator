import qrcode as qr
import qrcode.main

img = qr.make("https://www.youtube.com/")
img.save("YouTube.png")

qr1 = qrcode.main.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H,
                         box_size=10, border=10,)

qr1.add_data("https://www.google.co.in/maps/preview")
qr1.make(fit=True)
img1 = qr1.make_image(fill_color="white", back_color="black")
img1.save("GoogleMaps.png")

