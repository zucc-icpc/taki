from django.urls import path
from reports.views import ReportList, ReportDetail

urlpatterns = [
    path('reports/', ReportList.as_view(), name='report-list'),
    path('reports/<int:pk>/', ReportDetail.as_view(), name='report-detail'),
]