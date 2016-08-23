from flask import render_template, flash, redirect, request
from app import app
from .forms import ImageURLForm
from .clustering import clusters

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = ImageURLForm()
    if form.validate_on_submit():
        return render_template("analysis.html")
    return render_template("index.html", form=form)


@app.route("/analysis", methods=['POST'])
def analysis():
    if request.method == 'POST':
        form = request.form
        url = form.get("image_url")
        n = form.get("n")
        colors = clusters(url, n)
        print url
        print n
        print "successfully sent to function"
        return render_template("analysis.html", colors=colors)
    return render_template("analysis.html")