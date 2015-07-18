from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext

from web.utils import fb_sc_login_required

@fb_sc_login_required
def index(request):
    return render_to_response("index.html", RequestContext(request))

def login(request):
    return render_to_response("login.html", RequestContext(request))
