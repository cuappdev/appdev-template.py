from flask import request, render_template, jsonify, redirect
from appdev.controllers import *

from app.dao import users_dao

from app.models._all import *

# serializers
user_schema = UserSchema()
