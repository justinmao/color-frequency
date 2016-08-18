from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

class ImageURLForm(Form):
    image_url = StringField("image_url", validators = [DataRequired()])