from rest_framework import viewsets
from meituan.models import Merchant
from .serializers import MerchantSerializer
from rest_framework.authentication import BasicAuthentication,SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly
from .authentications import generate_jwt,JWTAuthentication
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .permissions import MyPermission

User = get_user_model()


class MerchantViewSet(viewsets.ModelViewSet):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer

    # authentication_classes：用来验证用户是否已经成功登录
    authentication_classes = [JWTAuthentication,BasicAuthentication]
    # permission_classes：用来根据用户的权限来限制访问
    # permission_classes = [IsAuthenticated]
    # permission_classes = [IsAuthenticated,IsAdminUser]
    permission_classes = [MyPermission]

    # AUTHORIZATION
    # basic usermae:password
    # createsuperuser 创建超级用户

@api_view(['GET'])
def token_view(request):
    token = generate_jwt(User.objects.first())
    return Response({"token":token})