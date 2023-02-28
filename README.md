# Learning Log

Learning Log is a simple Django application for creating a log of users learning progress.

## Overview

It has a registration and log in functionality with an admin page for the superuser.

Users can add/edit Topics and Entries in the respective topics.

![LearningLog-screenshot](https://user-images.githubusercontent.com/89355282/221864599-ba366526-6c99-4cc3-a577-4bef4a1cb326.png)

## Set up

There are some prerequisites to start using the Learning Log app:

App was created using Python `v.3.8.9`

1. Install **Django** framework on your local machine

`python -m pip install django`

2. Install **django-bootstrap4** module on your local machine

`python -m pip install django-bootstrap4`

3. Install **python-dotenv** module to use Environment Variables in Django to protect your secrets or database information ie. `SECRET_KEY`.

* `python -m pip install python-dotenv`
* Create a `.env` file at the root of the Project where `manage.py` file is.
* Set Environment Variables in `.env` file for example `SECRET_KEY='your secret key here'`. *You can generate your SECRET_KEY with a tool like [Djecrety](https://djecrety.ir/).*
* Assign the Environment Variables in the `settings.py`
* If you plan to host your Learning Log on the remote repository remember to add the `.env` file to `.gitignore` file.

4. Run the Learning Log app with a built-in local Django server.

`python manage.py runserver`

## Feedback and questions

I would appreciate any feedback or welcome any questions you might have. You can find my contact information in the bio or on my [website](https://jarekpacocha.online).
