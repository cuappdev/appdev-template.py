import sys
import os
import shutil

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def setup_dbs():
  print 'Setting up databases...'
  os.chdir('..')
  os.system('python manage.py db init')
  os.system('python manage.py db migrate')
  os.system('python manage.py db upgrade')
  os.chdir('scripts')
  print 'Finished setting up databases...'

def delete_migrations():
  try:
    os.chdir('..')
    shutil.rmtree('migrations')
    os.system('mysql --user={} --password={} --host={} {} '
              .format(os.environ['DB_USERNAME'], os.environ['DB_PASSWORD'],
                      os.environ['DB_HOST'], os.environ['DB_NAME'])
              + '--execute "drop table alembic_version"')
    os.chdir('scripts')
    print 'Migrations folder deleted...'

  except OSError:
    os.chdir('scripts')
    print 'No migrations folder to delete...'

if __name__ == '__main__':
  delete_migrations()
  setup_dbs()
