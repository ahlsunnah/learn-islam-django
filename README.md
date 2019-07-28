# Learn Islam django

<a href="https://circleci.com/gh/ahlsunnah/learn-islam-django" title="Current CircleCI build status.">
<img src="https://img.shields.io/circleci/build/github/ahlsunnah/learn-islam-django?label=tests&style=plastic" alt="Current CircleCI build status." />
</a>

<a href="https://github.com/pydanny/cookiecutter-django/" title="Built with Cookiecutter Django">
<img src="https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg" alt="Built with Cookiecutter Django" />
</a>

<a href="https://github.com/ambv/black" title="Black code style">
<img src="https://img.shields.io/badge/code%20style-Black-000000.svg" alt="Black code style
" />
</a>

# Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

# Basic Commands

## Setting Up Your Users

- To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.
- To create an **superuser account**, use this command:

      $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

## Type checks

Running type checks with mypy:

    $ mypy learn_islam

## Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

### Running tests with py.test

    $ pytest

## Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS compilation](http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html).

## Celery

This app comes with Celery.

To run a celery worker:

```{.sourceCode .bash}
cd learn_islam
celery -A config.celery_app worker -l info
```

Please note: For Celery's import magic to work, it is important _where_ the celery commands are run. If you are in the same folder with _manage.py_, you should be right.

## Email Server

In development, it is often nice to be able to see emails that are being sent from your application. For that reason local SMTP server [MailHog](https://github.com/mailhog/MailHog) with a web interface is available as docker container.

Container mailhog will start automatically when you will run all docker containers. Please check [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html) for more details how to start all containers.

With MailHog running, to view messages that are sent by your application, open your browser and go to `http://127.0.0.1:8025`

## Sentry

Sentry is an error logging aggregator service. You can sign up for a free account at <https://sentry.io/signup/?code=cookiecutter> or download and host it yourself. The system is setup with reasonable defaults, including 404 logging and integration with the WSGI application.

You must set the DSN url in production.

# Deployment

The following details how to deploy this application.

## Heroku

See detailed [cookiecutter-django Heroku documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-on-heroku.html).

## Docker

See detailed [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).
