import json

from django.http import HttpResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from django_pusher.push import pusher


@require_POST
@csrf_exempt
def pusher_auth(request):
    channel = request.POST["channel_name"]
    socket_id = request.POST["socket_id"]
    
    if pusher.allow_connection(request, channel):
        r = pusher._real_getitem(channel).authenticate(socket_id)
        return HttpResponse(json.dumps(r), mimetype="application/json")
    return HttpResponseForbidden("Not Authorized")
