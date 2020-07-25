import firebase_admin
from firebase_admin import firestore

firebase_admin.initialize_app()

db = firestore.client()


def save_image(image, read_image):
    dosya = open(f'assets/images/{image.filename}', 'wb')
    dosya.write(read_image)
    dosya.close()

    db.collection(u'images').add({
        "description": "",
        "like": False,
        "url": f'assets/images/{image.filename}'
    })
