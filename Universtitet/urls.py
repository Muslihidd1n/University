
from django.contrib import admin
from django.urls import path
from Asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hamma_fanlar/', hamma_fanlar),
]
