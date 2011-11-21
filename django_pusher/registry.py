from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

from django.contrib.sites.models import Site

from pusher import Pusher as PusherAPI


class NonUniqueNamespace(Exception):
    """
    Raised when you try to register a namespace that has already been registered.
    """


class UnregisteredNamespace(Exception):
    """
    Raised when you try and send a message to a channel that has not been registered.
    """


class Pusher(PusherAPI):
    
    def __init__(self, app_id=None, key=None, secret=None, **kwargs):
        self._registry = set()
        
        if not hasattr(settings, "PUSHER_APP_ID") and app_id is None:
            raise ImproperlyConfigured("PUSHER_APP_ID must be set or app_id must be passed to Pusher")
        if not hasattr(settings, "PUSHER_KEY") and key is None:
            raise ImproperlyConfigured("PUSHER_KEY must be set or key must be passed to Pusher")
        if not hasattr(settings, "PUSHER_SECRET") and secret is None:
            raise ImproperlyConfigured("PUSHER_SECRET must be set or secret must be passed to Pusher")
        
        kw = {
            "app_id": settings.PUSHER_APP_ID,
            "key": settings.PUSHER_KEY,
            "secret": settings.PUSHER_SECRET,
        }
        kw.update(kwargs)
        
        super(Pusher, self).__init__(**kw)
    
    def __getitem__(self, key):
        if key not in self._registry and [x for x in self._registry if key.startswith(x)]:
            raise UnregisteredNamespace("%s has not been registered." % key)
        return super(Pusher, self).__getitem__(self.make_key(key))
    
    def make_key(self, key):
        if getattr("PUSHER_SITE_SPECIFIC_CHANNELS", False):
            current_site = Site.objects.get_current()
            return "%s@%s" % (key, current_site.pk)
        return key
    
    def register(self, name):
        """
        Registers a unique namespace with django_pusher.
        """
        if name in self._registry:
            raise NonUniqueNamespace("%s has already been registered." % name)
        self._registry.add(name)
    
    def unregister(self, name):
        """
        Unregisters a unique namespace from django_pusher.
        """
        self._registry.discard(name)
