from django.urls import path, include
from user import views

urlpatterns = [
    path('user/', views.UserList.as_view(), name='user-list'),
    path('user/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('profile/', views.ProfileList.as_view(), name='profile-list'),
    path('profile/<int:pk>', views.ProfileDetail.as_view(), name='profile-detail')
]
