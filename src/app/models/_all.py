from marshmallow_sqlalchemy import ModelSchema

from app.models.user import *

class UserSchema(ModelSchema):
  class Meta(ModelSchema.Meta):
    model = User
