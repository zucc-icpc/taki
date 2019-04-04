from django.urls import path
from solutions.views import SolutionList, SolutionDetail

urlpatterns = [
    path('solutions/', SolutionList.as_view(), name='solution-list'),
    path('solutions/<int:pk>/', SolutionDetail.as_view(), name='solution-detail'),
]