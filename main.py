from flask import Flask,render_template,request
from qrcodegen import Qrcode_convertor


app = Flask(__name__)
output_folder = "static/qr_code_img"
@app.route("/", methods=["GET","POST"])
def home():
    qr_img = None
    if request.method == "POST":
        url = request.form["url"].strip()
        if url:
            qr_img = Qrcode_convertor(url,output_folder=output_folder)

    return render_template("frontpage.html",qr_image=qr_img)