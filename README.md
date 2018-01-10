# Microblog 

That project follow the Mega Tutorial made by **Miguel Grinberg** about flask and your resources.

For more information check the link below:

- [Miguel Grinberg Site](https://blog.miguelgrinberg.com/index)
- [Kickstarter](https://learn.miguelgrinberg.com/)

### Requirements

 - [Python 3+](https://www.python.org/)
 - [Pip](https://pypi.python.org/pypi/pip)
 - [Pipenv](https://github.com/pypa/pipenv)
 - [SQLite](https://www.sqlite.org/)

### Setup

Clone the project to your computer

```shell
git clone git@github.com:flaviovisetti/microblog-flask.git
```

Inside the folder, install all dependencies

```shell
pipenv install --dev --three
```

Activate the virtualenv to isolate the environment

```shell
pipenv shell
```

Create the tables in SQLite (Migrations)
*Remember to activate the virtualenv*

```shell
export FLASK_APP=microblog.py
flask db migrate
```

Run the project
*Remember to activate the virtualenv*

```shell
export FLASK_APP=microblog.py
flask run
```

The application will be available in `http://localhost:5000`