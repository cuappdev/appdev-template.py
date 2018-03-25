from . import *

class HelloWorldController(AppDevController):

  def get_path(self):
    return '/'

  def get_methods(self):
    return ['GET']

  def content(self, **kwargs):
    return {"hello": "world"}
