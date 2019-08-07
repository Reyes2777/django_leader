README
======

This is a test about leader django, is application build in Django Framework with postgresql

Installation
------------

#. Clone repo: ``git clone git@github.com:Reyes2777/django_leader.git``

#. Install requirements: ``pip install -r requirements.txt``

#. Create .env_server file with the following variables:

    * DEFAULT_DB_NAME=leader_django
    * DEFAULT_DB_HOST=localhost
    * DEFAULT_DB_HOST_PORT=5432
    * DEFAULT_DB_USER=guest
    * DEFAULT_DB_PASSWORD=guest

#. Enable precommit: ``pre-commit install``

#. Generate Documentation in format HTML with the following command inside folder docs : ``make html``

#. You can run Project in dev local with the next commands: ``docker-compose build`` ``docker-compose up``


Testing
-------

Run all tests with ``pytest -s -vvvv``. For more uses of pytest, `check this <https://docs.pytest.org/en/latest/usage.html>`_.

Alternatively you can run ``sh run_tests.sh``
