from django.contrib import admin
from django.conf.urls import url # this is for Django V1 , V2 should use "path"
from django.conf.urls import include


urlpatterns = [
    url('polls/', include('polls.urls')),
    url('admin/', admin.site.urls),
]
