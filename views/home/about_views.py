import os

import requests
from flask import request, session, redirect, url_for, render_template, Blueprint

blueprint = Blueprint('about', __name__, template_folder='templates')


@blueprint.route("/about", methods=['GET'])
def about():
    return render_template("home/about.html")
