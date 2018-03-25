import os
import sys

from app import app
from app.models._all import *
from app.utils.db_utils import *

src_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/src'
sys.path.append(src_path)
