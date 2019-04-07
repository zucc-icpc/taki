from honors.views import HonorList
from django.urls import path

urlpatterns = [
    path('honors/', HonorList.as_view(), name='honor-list'),
]