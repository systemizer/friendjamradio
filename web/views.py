from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from web.utils import DjangoSoundcloudClient


@login_required
def index(request):
    userid = request.GET.get("userid") or request.user.id
    user = get_object_or_404(User, pk=userid)
    client = DjangoSoundcloudClient(user)

    tracks = [s['origin'] for s in
              client.get("/me/activities", limit=50).obj['collection']]

    users = User.objects.all()
    return render_to_response("index.html",
                              {"tracks": tracks, "users": users,
                               "cur_user": user},
                              RequestContext(request))

def login(request):
    return render_to_response("login.html", RequestContext(request))
