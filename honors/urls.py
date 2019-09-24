from honors.views import HonorList, HonorDetail
from django.urls import path

urlpatterns = [
    path('honors/', HonorList.as_view(), name='honor-list'),
    path('honors/<int:pk>/', HonorDetail.as_view(), name='honor-detail'),
]
