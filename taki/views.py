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
        'user': reverse('user-list', request=request, format=format),
        'profile': reverse('profile-list', request=request, format=format),
        'solutions': reverse('solution-list', request=request, format=format),
        'templates': reverse('template-list', request=request, format=format),
        'verify-user': reverse('verify-user', request=request, format=format)
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
        return Response({"error": serializer.errors})


class ClearCookieJSONWebToken(ObtainJSONWebToken):
    """
    接受post请求生成JWT-Token并设置cookie
    """

    def post(self, request, *args, **kwargs):
        res = Response()
        res.set_cookie(api_settings.JWT_AUTH_HEADER_PREFIX.upper(), httponly=True, expires=datetime.now())
        return res