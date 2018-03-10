from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from prices.views import PricesView

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'api/v1/prices', PricesView.as_view())
]
