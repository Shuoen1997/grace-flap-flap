import os
import requests
import json
from dotenv import load_dotenv, find_dotenv
from flask import Flask, request, abort, render_template, redirect, url_for, Response

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)
load_dotenv(find_dotenv())

# Channel Access Token
channel_access_token = os.getenv('CHANNEL_ACCESS_TOKEN')
line_bot_api = LineBotApi(channel_access_token)

# Channel Secret
channel_secret = os.getenv('CHANNEL_SECRET')
handler = WebhookHandler(channel_secret)

permitted = False


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        password = request.form['password']
        if password != '123456':
            return "You don't have access to this page"
    if request.method == 'GET':
        return render_template('home.html')
    global permitted
    permitted = True
    return redirect(url_for("main"))


@app.route("/main", methods=['GET', 'POST'])
def main():
    global permitted
    if not permitted:
        return "You cannot directly access this page!"
    if request.method == 'POST':
        message = request.form['message-context']
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
            return "SUCCESS. Message sent: " + message

    return render_template('main.html')


# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text
    if text == "hello":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="hello there!"))
    elif text == "bye":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="bye :("))


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
