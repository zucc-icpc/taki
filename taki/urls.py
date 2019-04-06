"""taki URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token
from taki.views import CookieJSONWebToken, api_root, ClearCookieJSONWebToken
from django.conf.urls.static import static
from taki import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('article.urls')),
    path('api/', include('user.urls')),
    path('api/', include('solutions.urls')),
    path('api/', include('templates.urls')),
    path('', api_root)
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns += [
    path('api-token-auth/', CookieJSONWebToken.as_view()),
    path('clear-token/', ClearCookieJSONWebToken.as_view()),
    path('api-token-verify/',  verify_jwt_token)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)