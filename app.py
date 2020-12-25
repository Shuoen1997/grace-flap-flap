import os
from dotenv import load_dotenv, find_dotenv
from flask import Flask, request, abort

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