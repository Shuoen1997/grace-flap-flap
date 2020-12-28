import os

import requests
from flask import request, session, redirect, url_for, render_template, Blueprint

blueprint = Blueprint('user', __name__, template_folder='templates')


@blueprint.route("/<string:user_id>/viewlist", methods=['GET'])
def viewlist_for(user_id:str):
    return "Here are the grateful list for {}".format(user_id)
