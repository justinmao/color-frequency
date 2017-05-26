from flask import render_template, flash, redirect, request
from app import app
from .forms import ImageURLForm
from .main import get_palette


@app.route('/', methods=['GET', 'POST'])
def index():
    form = ImageURLForm()
    if request.method == "POST":  # img_form.validate_on_submit():
        data = request.form
        url = data.get("image_url")
        n = data.get("n")
        colors = get_palette(url, n)
        return render_template("results.html", form=form, image_url=url,
                               colors=colors)
    return render_template("home.html", form=form)