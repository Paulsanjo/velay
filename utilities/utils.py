import os
import re
import secrets
import fnmatch
from core import app
from PIL import Image
from marshmallow import ValidationError


class Tools():
    """Validation and input cleanup for serialization for the schemas that require it, to ensure
        DRY within this codebase"""

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
        """validator for phone numbers entering the system, this function does not contain a self parameter in the function
        declaration."""

        pattern = re.compile(r"\d{10}")
        if not pattern.search(str(data)):
            raise ValidationError("Invalid number")

    def password_strength(data):
        """password validation to ensure minimum password strength, this function does not contain a self parameter in the function
        declaration."""

        pattern = re.compile(r"(([\W+_])([A-Z]))")
        num = re.compile(r"\d+")

        try:
            if not pattern.search(data).group(2) and pattern.search(data).group(3):
                raise ValidationError("""
                        Password must contain at least 8 characters, one numeric, one special and one Uppercase
                     """)
            elif not num.findall(data):
                raise ValidationError("""
                        Password must contain at least 8 characters, one numeric, one special and one Uppercase
                     """)
            elif len(data) < 8 or len(data) > 15:
                raise ValidationError("Password cannot be less than 8 characters")
        except Exception:
            raise ValidationError("""
                        Password must contain at least 8 characters one numeric, one special and one Uppercase
                     """)

    def upload(file):
        """file validation and handling for images in the system"""

        if not fnmatch.fnmatch(file, "*.jpg") or fnmatch.fnmatch(file, "*.png"):
            raise ValidationError("not a valid image")
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
