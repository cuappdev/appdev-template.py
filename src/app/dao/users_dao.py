from . import *

def get_user_by_id(user_id):
  return User.query.filter(User.id == user_id).first()

def create_user(email, first_name='', last_name=''):
  optional_user = get_user_by_id(email)

  if optional_user is not None:
    return False, optional_user

  # user does not exist
  user = User(
      email=email,
      first_name=first_name,
      last_name=last_name,
  )
  db_utils.commit_model(user)
  return True, user
