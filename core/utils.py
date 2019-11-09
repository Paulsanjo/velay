import os
import secrets
import fnmatch
from . import app
from PIL import Image


def upload(file):
    if not fnmatch.fnmatch(file, "*.jpg") or fnmatch.fnmatch(file, "*.png"):
        return "Invalid file, select an file "
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(file)
    product_image = random_hex + f_ext
    image_path = os.path.join(app.root_path,
                              "static/images", product_image)
    thumbnail = (128, 128)
    i = Image.open(file)
    i.thumbnail(thumbnail)
    i.save(image_path)
    return product_image
