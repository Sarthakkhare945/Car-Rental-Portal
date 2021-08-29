# Car-Rental-Portal

It is an online system through which customers canview
available cars, view profile and book car.

Flask
=====

Flask is a lightweight <a href='https://wsgi.readthedocs.io/en/latest/'>WSGI</a> web application framework. It is designed
to make getting started quick and easy, with the ability to scale up to
complex applications. It began as a simple wrapper around <a href='https://werkzeug.palletsprojects.com'>Werkzeug</a>
and <a href='https://jinja.palletsprojects.com'>Jinja</a> and has become one of the most popular Python web
application frameworks.

Flask offers suggestions, but doesn't enforce any dependencies or
project layout. It is up to the developer to choose the tools and
libraries they want to use. There are many extensions provided by the
community that make adding new functionality easy.


Installing
----------

Install and update using <a href='https://pip.pypa.io/en/stable/quickstart/'>pip</a>:



    $ pip install -U Flask




A Simple Example
----------------



    # save this as app.py
    from flask import Flask

    app = Flask(__name__)

    @app.route("/")
    def hello():
        return "Hello, World!"



    $ flask run
      * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)


Contributing
------------

For guidance on setting up a development environment and how to make a
contribution to Flask, see the <a href='https://github.com/pallets/flask/blob/master/CONTRIBUTING.rst'>contributing guidelines</a>.




Donate
------

The Pallets organization develops and supports Flask and the libraries
it uses. In order to grow the community of contributors and users, and
allow the maintainers to devote more time to the projects, <a href='https://palletsprojects.com/donate'>please
donate today</a>.




Links
-----

-   Documentation: https://flask.palletsprojects.com/
-   Changes: https://flask.palletsprojects.com/changes/
-   PyPI Releases: https://pypi.org/project/Flask/
-   Source Code: https://github.com/pallets/flask/
-   Issue Tracker: https://github.com/pallets/flask/issues/
-   Website: https://palletsprojects.com/p/flask/
-   Twitter: https://twitter.com/PalletsTeam
-   Chat: https://discord.gg/pallets





