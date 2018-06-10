"""RestApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
import xadmin
from rest_framework.authtoken import views
from RestApi.settings import MEDIA_ROOT
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from goods.views import GoodsListViewSet,CategoryViewSet
from rest_framework_jwt.views import obtain_jwt_token
from users.views import SmsCodeViewset,UserViewset
from blog.views import ArticlesListViewSet, AllLabelsViewSet, HomeArticlesListViewSet,BlogImageUploadSet,TaskUploadSet
router = DefaultRouter()
# 商品
router.register(r'goods',GoodsListViewSet)
router.register(r'homeArticles',HomeArticlesListViewSet)
# 商品分类
router.register(r'categorys',CategoryViewSet)
router.register(r'code', SmsCodeViewset, base_name="code")
router.register(r'users', UserViewset, base_name="users")
router.register(r'articles',ArticlesListViewSet)
router.register(r'labels',AllLabelsViewSet)
router.register(r'blogimage',BlogImageUploadSet)
router.register(r'imgtask',TaskUploadSet)
# good_list = GoodsListViewSet.as_view({
#      'get':'list',
# })

urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^media/(?P<path>.*)$' , serve , {"document_root": MEDIA_ROOT}) ,

    # drf自带的token认证模式
    url(r'^api-token-auth/' , views.obtain_auth_token) ,

    # jwt的认证接口
    url(r'^login/' , obtain_jwt_token) ,
    #商品列表页
     url(r'^', include(router.urls)),
    # url(r'goods/$',good_list,name="goods-list"),

    url(r'doc/',include_docs_urls(title="api实践"))


]
