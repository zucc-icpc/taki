from django.urls import path
from snippet.views import SnippetList, SnippetDetail

urlpatterns = [
    path('snippet/', SnippetList.as_view(), name='snippet-list'),
    path('snippet/<int:pk>/', SnippetDetail.as_view(), name='snippet-detail'),
]