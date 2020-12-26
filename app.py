import os
from dotenv import load_dotenv, find_dotenv
from flask import Flask

app = Flask(__name__)


def run_app():
    load_dotenv(find_dotenv())
    app.secret_key = bytes(os.getenv('SESSION_KEY'), "utf-8").decode('unicode_escape')
    register_blueprints()
    app.run(host='0.0.0.0', port=5000, debug=True)


def register_blueprints():
    from views.admin import send_message_views
    from views.receiver import receive_views

    app.register_blueprint(send_message_views.blueprint)
    app.register_blueprint(receive_views.blueprint)


if __name__ == "__main__":
    run_app()

