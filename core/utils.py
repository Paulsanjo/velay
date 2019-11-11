import os
import re
import secrets
import fnmatch
from . import app
from PIL import Image
from marshmallow import ValidationError


class Tools():
    """Validation and input cleanup for serialization for the schemas that require it, to ensure
        DRY rule within this codebase"""

    def setup(self, obj):
        obj = obj.strip()
        return obj

    def load_name(self, value):
        pattern = re.compile(r"\w")
        if not pattern.search(value):
            raise ValidationError("No special characters allowed")
        else:
            return value

    def contact(data):
        """validator for phone numbers entering the system"""
        pattern = re.compile(r"\d{6,15}")
        if not pattern.search(str(data)):
            raise ValidationError("Invalid number")

    def upload(file):
        if not fnmatch.fnmatch(file, "*.jpg") or fnmatch.fnmatch(file, "*.png"):
            return "Invalid, select a valid image "
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
