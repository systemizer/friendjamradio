from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from web.utils import soundcloud_client_for_user


@login_required
def index(request, userid=None):
    user = get_object_or_404(User, pk=userid or request.user.id)
    client = soundcloud_client_for_user(user)

    tracks = [s['origin'] for s in
              client.get("/me/activities", limit=50).obj['collection']]

    return render_to_response("index.html", {"tracks": tracks},
                              RequestContext(request))

def login(request):
    return render_to_response("login.html", RequestContext(request))
