# flask boilerplate code

### packages

- python-dotenv
- pipenv

### flask extensions

- flask-wtf
- flask-sqlalchemy
- flask-migrate
- flask-login
- flask-mail

### frontend packages

- bootstrap
- jquery

## How to start

note: using npm from inside python virtual environment gave me errors, deactivate the virtual environment before using npm

- rename .env-example to .env

### (windows)
- `cd app\static`
- `npm install`
- `cd ..\..`
- `python -m venv venv`
- `venv\Scripts\activate`
- `pip install pipenv`
- `pipenv install`

### (linux)
- `cd app/static`
- `npm install`
- `cd ../..`
- `python3 -m venv venv`
- `source venv/bin/activate`
- `pip install pipenv`
- `pipenv install`

### testing

- run the command `flask test`

all is good.
