from django.urls import path
from app.views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),
]
