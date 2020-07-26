from datetime import datetime

import firebase_admin
from firebase_admin import firestore, storage


firebase_admin.initialize_app()

db = firestore.client()
bucket = storage.bucket("petstories.appspot.com")


def save_image(image, read_image):
    blob = bucket.blob(f'assets/images/{image.filename}')
    blob.upload_from_string(read_image, content_type=image.content_type)

    db.collection(u'images').add({
        "description": "",
        "like": False,
        "url": blob.generate_signed_url(datetime(2100, 11, 11))
    })
