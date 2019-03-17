from django.urls import path, include
from article.views import ArticleList, ArticleDetail

urlpatterns = [
    path('article/', ArticleList.as_view(), name='article-list'),
    path('article/<int:pk>', ArticleDetail.as_view(), name='article-detail'),
]
