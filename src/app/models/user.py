from . import *

class User(Base):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  first_name = db.Column(db.String(255))
  last_name = db.Column(db.String(255))

  def __init__(self, **kwargs):
    self.first_name = kwargs.get('first_name')
    self.last_name = kwargs.get('last_name')
