from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

from django.contrib.site.models import Site

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
    
    def __init__(self):
        self._registry = set()
        
        if not hasattr(settings, "PUSHER_APP_ID"):
            raise ImproperlyConfigured("PUSHER_APP_ID must be set!")
        if not hasattr(settings, "PUSHER_KEY"):
            raise ImproperlyConfigured("PUSHER_KEY must be set!")
        if not hasattr(settings, "PUSHER_SECRET"):
            raise ImproperlyConfigured("PUSHER_SECRET must be set!")
        
        kw = {
            "app_id": settings.PUSHER_APP_ID,
            "key": settings.PUSHER_KEY,
            "secret": settings.PUSHER_SECRET,
        }
        
        super(Pusher, self).__init__(**kw)
    
    def __getitem__(self, key):
        if key not in self._registry:
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
