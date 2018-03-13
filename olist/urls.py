from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework_swagger.views import get_swagger_view

from call.views import CallView

schema_view = get_swagger_view(title='Work To Olist')

urlpatterns = [
    url(r'^', include('price.urls')),
    path('admin/', admin.site.urls),
    url(r'^docs/$', schema_view),
    url(r'^api/v1/calls/$', CallView.as_view()),
]
