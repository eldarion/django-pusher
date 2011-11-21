from django.conf.urls.defaults import patterns, url

urlpatterns = patterns("",
    url("^auth/$", "django_pusher.views.pusher_auth", name="pusher_auth"),
)
