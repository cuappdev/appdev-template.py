# AppDev Python Backend Template

This is a template for writing AppDev backends in Python. We use the following technologies:

1. Flask (Routes)
2. SQLAlchemy + Marshmallow (ORM + Serializing)
4. MySQL (DB)
5. Nosetests (Testing)

It includes a basic "hello, world!" endpoint, and a basic user model.

## Virtualenv

Virtualenv setup!

```bash
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
pip install git+https://github.com/cuappdev/appdev.py.git --upgrade
```

## Environment Variables
It's recommended to use [`autoenv`](https://github.com/kennethreitz/autoenv). 
The `pip` installation specified in the README doesn't seem to work, so installing globally is recommended.

The required environment variables for this API are the following:

```bash
export DB_USERNAME=CHANGE_ME
export DB_PASSWORD=CHANGE_ME
export DB_HOST=localhost
export DB_NAME=templatedb
export APP_SETTINGS=config.CHANGE_ME
```

To source the `.env` file, make a local copy of the `template` file. 
`cd` out of the directory, and `cd` back and you should be prompted by `autoenv`.

```bash
cp env.template .env
```

## Setting Up Database
Ensure you have `mysql` plus command line tools setup:
```bash
mysql -u root -p
mysql> CREATE DATABASE templatedb;
mysql> \q
cd src
python manage.py db init  
```

## Updating the Database
To update the database with changes you make, run the following:
```bash
python manage.py db migrate
python manage.py db upgrade
```

## Testing

To test, run `nosetests` from the root of this repo.

## Running the Server

To run the server, run:

```bash
python manage.py runserver
```

The hello-world endpoint can be found at: http://127.0.0.1:5000/api/v0/
