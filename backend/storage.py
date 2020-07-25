

def save_image(image, read_image):
    dosya = open(f'assets/images/{image.filename}', 'wb')
    dosya.write(read_image)
    dosya.close()
