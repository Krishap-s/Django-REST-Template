# Django-REST-boilerplate
[![Test](https://github.com/Krishap-s/Django-REST-boilerplate/actions/workflows/main.yml/badge.svg)](https://github.com/Krishap-s/Django-REST-boilerplate/actions/workflows/main.yml)
[![codecov](https://codecov.io/gh/Krishap-s/Django-REST-boilerplate/branch/main/graph/badge.svg?token=FFBEISOEF8)](https://codecov.io/gh/Krishap-s/Django-REST-boilerplate)

*Sometimes you have to fly before you crawl*

A preset and reliable django boilerplate for projects with ridiculously short deadlines. Django-REST-template helps with providing all initial backend devops out of box, so that you can focus on other important things.

## Features
- Depandabot updates 
- Testing and codecoverage with tox
- Linting

## Installation
```
python -m venv venv
pip install -r requirements.txt
./manage.py migrate
```
> Note: Change the badge urls to your project's current repository

## Run server
```
uvicorn --env-file .env server.asgi:application
```

## Testing
 > Note: Requires pyenv installed
```
pyenv install 3.7.x
pyenv install 3.8.x
pyenv install 3.9.x
pyenv install 3.10.x
tox -v
```
