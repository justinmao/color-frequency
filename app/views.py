from flask import render_template, flash, redirect
from app import app
from .forms import ImageURLForm
from .clustering import clusters

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = ImageURLForm()
    if form.validate_on_submit():
        flash("Image URL: %s" % form.image_url.data)
        colors = clusters(form.image_url.data, form.n.data)
        return render_template("analysis.html", test="fsfs")
    return render_template("index.html", form=form)


@app.route("/analysis", methods=['GET', 'POST'])
def analysis(s):
    return render_template("analysis.html", test=s)