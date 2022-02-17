

from django.urls import path
from .views import home, result


urlpatterns = [
   path('',home),
   path('result/',result)
]