from flask import Flask, request
import glob

from image_validator import image_has_pet


app = Flask(__name__, static_folder='assets')


def anasayfa_oluştur(images, message):
	return f'''
		<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
		<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap-theme.min.css">
		<script src="https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>

		<link rel="stylesheet" href="assets/style/style.css">

		<div class="text-center">
			<form action="/" method="POST" enctype="multipart/form-data">
				<div class="form-group">
				    <label for="myFile">Ev Hayvanı Yükleyiniz</label>
					<input class="form-control-file" type="file" id="myFile" name="image">
					<input type="submit" value="Yükle">
				</div>
			</form>
			{message}
		</div>

		<div class="text-center">
			{images}
		</div>
	'''


def resimleri_oluştur():
	images = ''
	for saved_image in glob.glob('assets/images/*.jpg'):
		images = images + f'<img class="rounded mx-auto d-block" src="{saved_image}" width="400" height="500"><br>'

	return images

@app.route('/', methods=["GET", "POST"])
def anasayfa():

	message = ''
	if request.method == "POST":
		image = request.files.get('image')
		read_image = image.read()
		if image_has_pet(read_image):

			dosya = open(f'assets/images/{image.filename}', 'wb')
			dosya.write(read_image)
			dosya.close()

			# image.save(f'assets/images/{image.filename}')


		else:
			message = 'Ev Hayvanı Dışında Fotoğraf Paylaşamazsınız!'


	images = resimleri_oluştur()
	return anasayfa_oluştur(images, message)





app.run()






