from flask import render_template, redirect
from app import app
from .forms import ImageURLForm
from .clustering import clusters

@app.route('/')
@app.route('/index')
def index():
    form = ImageURLForm()
    if form.validate_on_submit():
        return redirect("/")
    return render_template("index.html")
