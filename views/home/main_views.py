import os

import requests
from flask import request, session, redirect, url_for, render_template, Blueprint

blueprint = Blueprint('main', __name__, template_folder='templates')


@blueprint.route("/", methods=['GET'])
def index():
    return redirect(url_for(".home"))


@blueprint.route("/home", methods=['GET'])
def home():
    return render_template("home.html")
