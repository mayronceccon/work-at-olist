from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

from price.views import PriceView

schema_view = get_swagger_view(title='Work To Olist')

urlpatterns = [
    url(r'^docs/$', schema_view),
    path('admin/', admin.site.urls),
    url(r'api/v1/prices', PriceView.as_view())
]
