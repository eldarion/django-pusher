Django Pusher
=============

.. image:: https://img.shields.io/travis/eldarion/django-pusher.svg
    :target: https://travis-ci.org/eldarion/django-pusher

.. image:: https://img.shields.io/coveralls/eldarion/django-pusher.svg
    :target: https://coveralls.io/r/eldarion/django-pusher

.. image:: https://img.shields.io/pypi/dm/django-pusher.svg
    :target:  https://pypi.python.org/pypi/django-pusher/

.. image:: https://img.shields.io/pypi/v/django-pusher.svg
    :target:  https://pypi.python.org/pypi/django-pusher/

.. image:: https://img.shields.io/badge/license-BSD-blue.svg
    :target:  https://pypi.python.org/pypi/django-pusher/


Django Pusher is an application that makes it easier to utilize pusher.com with reusable applications. It solves
the problem of authentication of private/presence channels as well as helping to prevent namespace clashes.

Usage
-----

Django Pusher provides a pusher object gotten by::

    from django_pusher.push import pusher

``pusher`` Mimics the Generic Python Library provided by pusher.com except it adds a ``register`` and ``unregister`` command.
