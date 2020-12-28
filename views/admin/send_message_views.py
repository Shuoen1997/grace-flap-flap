import os

import requests
from flask import request, session, redirect, url_for, render_template, Blueprint

blueprint = Blueprint('admin', __name__, template_folder='templates')


@blueprint.route("/admin/login", methods=['GET'])
def admin_login_get():
    return render_template("admin/login.html")


@blueprint.route("/admin/login", methods=['POST'])
def admin_login_post():
    if request.form['password'] == os.getenv('SECRET_PASSWORD'):
        session['authenticated'] = True
        return redirect(url_for('.admin_tool_get'))


@blueprint.route("/admin/tool", methods=['POST'])
def admin_tool_post():
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
        return render_template("admin/tool.html", message=message)


@blueprint.route("/admin/tool", methods=['GET'])
def admin_tool_get():
    if 'authenticated' not in session:
        return "Not permitted!"
    return render_template("admin/tool.html")
