from web import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^/users/(?P<userid>\d+)/$', views.index, name='index'),

    url(r'^login/$', views.login, name='login'),
]
