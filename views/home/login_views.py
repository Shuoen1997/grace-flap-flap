import os

import requests
from flask import request, session, redirect, url_for, render_template, Blueprint
from views.user.grateful_list_views import *

blueprint = Blueprint('login', __name__, template_folder='templates')


@blueprint.route("/login", methods=['GET'])
def login_get():
    return render_template("home/login.html")


@blueprint.route("/login", methods=['POST'])
def login_post():
    user_id = request.form['userid']
    return redirect(url_for('user.viewlist_for', user_id=str(user_id)))
