import os

import requests
from flask import request, session, redirect, url_for, render_template, Blueprint

blueprint = Blueprint('home', __name__, template_folder='templates')


@blueprint.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        password = request.form['password']
        if password == os.getenv('SECRET_PASSWORD'):
            session['authenticated'] = True
            return redirect(url_for("home.main"))
        else:
            return render_template("home.html", error="Incorrect password")
    if request.method == 'GET':
        return render_template("home.html")


@blueprint.route("/main", methods=['GET', 'POST'])
def main():
    if 'authenticated' not in session:
        return "Not permitted!"

    if request.method == 'POST':
        message = request.form['message-context'] or "nothing"
        channel_access_token = os.getenv('CHANNEL_ACCESS_TOKEN')
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {channel_access_token}'
        }
        data = {
            "to": "U68224c4538a68ae95239bb8a15807a1c",
            "messages": [{"type": "text", "text": message}]
        }
        try:
            r = requests.post(url='https://api.line.me/v2/bot/message/push', headers=headers, json=data)
            r.raise_for_status()
        except requests.RequestException as e:
            raise SystemExit(e)
        else:
            return render_template("main.html", message=message)

    return render_template("main.html")
