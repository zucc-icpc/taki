from django.urls import path
from solution.views import SolutionList, SolutionDetail

urlpatterns = [
    path('solution/', SolutionList.as_view(), name='solution-list'),
    path('solution/<int:pk>/', SolutionDetail.as_view(), name='solution-detail'),
]