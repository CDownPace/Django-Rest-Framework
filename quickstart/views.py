from rest_framework import viewsets
from meituan.models import Merchant
from .serializers import MerchantSerializer

# 这个视图函数已经包含了增删改检索
class MerchantViewset(viewsets.ModelViewSet):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer