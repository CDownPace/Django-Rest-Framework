import jwt
import time
from django.conf import settings
from rest_framework.authentication import BaseAuthentication,get_authorization_header
from rest_framework import exceptions
from django.contrib.auth import get_user_model
User = get_user_model()

def generate_jwt(user):
    timestamp = int(time.time()) + 60*60*24*7
    # timestamp = int(time.time()) + 2
    # 因为jwt.encode返回的是bytes数据类型，因此需要decode解码成str类型
    return jwt.encode({"userid":user.pk,"exp":timestamp},settings.SECRET_KEY).decode('utf-8')

class JWTAuthentication(BaseAuthentication):
    """
    Authorization: JWT 401f7ac837da42b97f613d789819ff93537bee6a
    """

    keyword = 'JWT'
    model = None

    def authenticate(self, request):
        auth = get_authorization_header(request).split()

        if not auth or auth[0].lower() != self.keyword.lower().encode():
            return None

        if len(auth) == 1:
            msg = 'Authorization 不可用！'
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = 'Authorization 不可用！应该提供一个空格！'
            raise exceptions.AuthenticationFailed(msg)

        try:
            jwt_token = auth[1]
            # 如果解码的时候，发现
            jwt_info = jwt.decode(jwt_token,settings.SECRET_KEY)
            userid = jwt_info.get('userid')
            try:
                user = User.objects.get(pk=userid)
                return (user,jwt_token)
            except:
                msg = "用户不存在！"
                raise exceptions.AuthenticationFailed(msg)
        except jwt.ExpiredSignatureError:
            msg = 'Token已经过期了！'
            raise exceptions.AuthenticationFailed(msg)