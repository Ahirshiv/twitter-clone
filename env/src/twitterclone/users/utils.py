import os, secrets
from PIL import Image
from flask import current_app

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, file_ext = os.path.splitext(form_picture.filename) # get file extension
    picture_fn = random_hex + file_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile-pictures', picture_fn)

    # resize image
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)

    # save picture to profile pictures folder
    i.save(picture_path)
    return picture_fn