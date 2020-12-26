import os
import requests
import json
from dotenv import load_dotenv, find_dotenv
from flask import request, abort, Blueprint, current_app

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

blueprint = Blueprint('receive', __name__, template_folder='templates')

load_dotenv(find_dotenv())
# Channel Access Token
channel_access_token = os.getenv('CHANNEL_ACCESS_TOKEN')
line_bot_api = LineBotApi(channel_access_token)
# Channel Secret
channel_secret = os.getenv('CHANNEL_SECRET')
handler = WebhookHandler(channel_secret)


# 監聽所有來自 /callback 的 Post Request
@blueprint.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    current_app.logger.info("Request body: " + body)
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
    current_app.logger.info("Received TEXT:" + text)
    if text == "hello":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="hello there!"))
    elif text == "bye":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="bye :("))
