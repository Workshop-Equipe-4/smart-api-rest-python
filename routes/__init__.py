from flask import Blueprint

routes = Blueprint('routes', __name__)

from .appartment import *
from .sensor import *
