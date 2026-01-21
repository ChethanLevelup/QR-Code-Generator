from qrcode import QRCode
import os
import uuid

def Qrcode_convertor(url,output_folder):
    # file path where should the qrcode should be saved
    os.makedirs(output_folder,exist_ok=True)
    filename = f"{uuid.uuid4()}.png"
    file_path = os.path.join(output_folder,filename)

    # qr code generation
    qr = QRCode(box_size=6,border=4)
    # add data you want to store inside qrcode
    qr.add_data(url)
    qr.make(fit=True)
    # create the qr image
    img = qr.make_image(fill_color="black",back_color="white")
    # save the image
    img.save(file_path)
    return file_path
