from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^api/v1/prices/(?P<pk>[0-9]+)$',
        views.get
    ),
    url(
        r'^api/v1/prices/$',
        views.get_all
    ),
]
