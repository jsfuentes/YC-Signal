# Python Base
This is a python flask base to build off of. It contains the following:
- flask_login setup
- mongoengine/mongolab setup
- factory method for different dev/prod configurations
- User model in MongoEngine
- example form
- example get and post routes
- pipenv runtime setup

## Running App
1. `pip install pipenv`
2. `pipenv install`, this handles your virtual environment using the Pipfile much like npm
3. `pipenv run export FLASK_APP=app.py`
4. `pipenv run flask run`, this puts Flask in debug mode and automatically reloads on changes

`pipenv run` should prefix anything you want to run in the environment i.e `pipenv install flask`
`pipenv shell` enters the virtual environment if you want to skip the prefixing
