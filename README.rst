Django Pusher
=============

Django Pusher is an application that makes it easier to utilize pusher.com with reusable applications. It solves
the problem of authentication of private/presence channels as well as helping to prevent namespace clashes.

Usage
-----

Django Pusher provides a pusher object gotten by::

    from django_pusher.push import pusher

``pusher`` Mimics the Generic Python Library provided by pusher.com except it adds a ``register`` and ``unregister`` command.
