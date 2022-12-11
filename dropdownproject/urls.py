from django.contrib import admin
from django.urls import path
from django.urls import path, include
#from dropdownlist import urls as dropdownlist
from api import urls as api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(api)),
]