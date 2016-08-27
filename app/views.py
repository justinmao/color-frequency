from flask import render_template, flash, redirect, request
from app import app
from .forms import ImageURLForm
from .main import get_palette


@app.route('/', methods=['GET', 'POST'])
def index():
    img_form = ImageURLForm()
    if img_form.validate_on_submit():
        form = request.form
        url = form.get("image_url")
        n = form.get("n")
        colors = get_palette(url, n)
        return render_template("index.html", form=img_form, image_url=url,
                               colors=colors)
    return render_template("index.html", form=img_form)
