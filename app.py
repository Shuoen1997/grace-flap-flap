import os
import logging
from dotenv import load_dotenv, find_dotenv
from flask import Flask



def create_app():
    app = Flask(__name__)
    load_dotenv(find_dotenv())
    app.secret_key = bytes(os.getenv('SESSION_KEY'), "utf-8").decode('unicode_escape')
    register_blueprints(app)
    return app


def run_app():
    app = create_app()
    app.logger.setLevel(logging.INFO)
    app.run(host='0.0.0.0', port=5000, debug=True)


def register_blueprints(app):
    from views.admin import send_message_views
    from views.receiver import receive_views
    from views.home import login_views, main_views
    from views.user import grateful_list_views

    app.register_blueprint(send_message_views.blueprint)
    app.register_blueprint(receive_views.blueprint)
    app.register_blueprint(login_views.blueprint)
    app.register_blueprint(main_views.blueprint)
    app.register_blueprint(grateful_list_views.blueprint)


if __name__ == "__main__":
    run_app()
