from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', home_view),
    path('MAIN/', MAIN),
    path('categories/', categories),
    path('categories/<int:catid>/', categories),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive)
]