from django.conf import settings


def pusher(request):
    return {
        "PUSHER_KEY": getattr(settings, "PUSHER_KEY", ""),
    }
