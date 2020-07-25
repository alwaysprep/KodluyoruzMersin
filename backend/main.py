import glob

from flask import Flask, request, jsonify
from flask_cors import CORS

from image_validator import image_has_pet
from storage import save_image

app = Flask(__name__, static_folder='assets')
CORS(app)


@app.route('/', methods=["POST"])
def anasayfa():

    image = request.files.get('image')
    read_image = image.read()
    if image_has_pet(read_image):
        save_image(image, read_image)
    else:
        return {'error': 'Ev Hayvanı Dışında Fotoğraf Paylaşamazsınız!'}, 400

    return {'status': 'Ok'}


app.run()
