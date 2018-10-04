# Python Base
This is a python flask base to build off of. It contains the following:
- flask_login setup
- mongoengine/mongolab setup
- factory method for different dev/prod configurations
- User model in MongoEngine
- example form
- example get and post routes
- pipenv runtime setup

## Setup App
1. `pip install pipenv`
2. In the main directory, `pipenv install`, this handles your virtual environment using the Pipfile much like npm
3. Follow the instructions in `example.env` to set your env variables/db or remove reference to the db

## Run App
1. `pipenv shell` enters the virtual environment
2. `flask run`, runs app.py with .env variables
- if you uncommented debug mode env variable its in debug mode and automatically reloads on changes

- Can also not shell and prefix any command with `pipenv run` i.e `pipenv run flask run``
