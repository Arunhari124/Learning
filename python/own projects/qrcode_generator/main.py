import qrcode

url=input("ENter the link=").strip()

file_path="code.png"

qr=qrcode.QRCode()
qr.add_data(url)
img=qr.make_image()
img.save(file_path)
print("Completed")