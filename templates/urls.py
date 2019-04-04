from templates.views import TemplateList, TemplateDetail
from django.urls import path

urlpatterns = [
    path('templates/', TemplateList.as_view(), name='template-list'),
    # path('templates/', TemplateCreate.as_view(), name='template-create'),
    path('templates/<int:pk>/', TemplateDetail.as_view(), name='template-detail')
]