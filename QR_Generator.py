import qrcode
data="https://wikipedia.com"
Image=qrcode.make(data)
Image.save("wikipedia.png")