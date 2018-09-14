from django.conf.urls import url
from . import views

urlpatterns = [
    # /issues/
    url(r'^$', views.index, name = 'index'),
    # /issues/1/
    url(r'^(?P<issue_id>[0-9]+)/$', views.detail, name = 'detail'),
    ]