from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from datetime import datetime
from rest_framework import status
from rest_framework_jwt.views import ObtainJSONWebToken, VerifyJSONWebToken
from rest_framework_jwt.settings import api_settings


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'article': reverse('article-list', request=request, format=format),
        'user': reverse('user-list', request=request, format=format),
        'profile': reverse('profile-list', request=request, format=format),
        'solution': reverse('solution-list', request=request, format=format),
        # 'upload': reverse('upload-avatar', request=request, format=format),
        # 'snippets': reverse('snippet-list', request=request, format=format)
    })


class CookieJSONWebToken(ObtainJSONWebToken):
    """
    接受post请求生成JWT-Token并设置cookie
    """

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user = serializer.object.get('user') or request.user
            token = serializer.object.get('token')
            response_data = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER(
                token, user, request)
            res = Response(response_data)
            res.set_cookie(api_settings.JWT_AUTH_HEADER_PREFIX.upper(), value=response_data[
                           'token'], httponly=True, expires=datetime.now() + api_settings.JWT_EXPIRATION_DELTA)
            return res
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CookieJSONWebTokenVerify(VerifyJSONWebToken):
    """
    接受post请求验证JWT-Token并设置cookie
    """

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            print(serializer.object)
            user = serializer.object.get('user') or request.user
            token = serializer.object.get('token')
            response_data = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER(
                token, user, request)
            res = Response(response_data)
            res.set_cookie(api_settings.JWT_AUTH_HEADER_PREFIX.upper(),
                           value=response_data['token'],
                           httponly=True,
                           expires=datetime.now() + api_settings.JWT_EXPIRATION_DELTA
                           )
            return res
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)