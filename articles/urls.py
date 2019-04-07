from django.urls import path
from articles.views import ArticleList, ArticleDetail

urlpatterns = [
    path('articles/', ArticleList.as_view(), name='articles-list'),
    path('articles/<int:pk>/', ArticleDetail.as_view(), name='articles-detail'),
]
