from flask import Flask, request,jsonify, render_template
import qrcode
# import pyzbar
import cv2


# # code =  request.form.get('code') 
c_barcode = 'http://qrco.de/bebUVc'

npn = Flask(__name__)

def n_barcode(decoded_qr_codes, data):
    # return(f'Sorry, It seems like you are a stranger.')
    if not decoded_qr_codes :
        # return render_template('.incorrect.html')
        return jsonify('The barcode you provided is incorrect.')
    else:
        if c_barcode:
            # return render_template('.index copy 2.html')
            print(data)
            return 'Successfully'  #come update later


if __name__ == "__main__":
    # scan_qr_code()
    npn.run(port=4620,debug=True)

