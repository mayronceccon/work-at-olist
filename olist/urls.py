from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from rest_framework.documentation import include_docs_urls

from prices.views import PricesView

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^docs/', include_docs_urls(
                title='Work To Olist',
                description='Documentation of project Work To Olist'
            )
        ),
    url(r'api/v1/prices', PricesView.as_view())
]
