from django.urls import path
from .views import MerchantView,MerthantListView,MerchantViewSet
from rest_framework.routers import DefaultRouter

app_name = 'classview'
urlpatterns = [
    # 列表：/merchant/ get
    # 新增：/merchant/ post
    # 详情：/merchant/[pk]/ get
    # 修改：/merchant/[pk]/ put
    # 删除：/merchant/[pk]/ delete
    path('merchant/',MerchantView.as_view()),
    path('merchant/<int:pk>/',MerchantView.as_view()),
    path('merchants/',MerthantListView.as_view())
]

router = DefaultRouter()
router.register('shangjia',MerchantViewSet,basename='shangjia')
urlpatterns += router.urls