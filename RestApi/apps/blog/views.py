from django.shortcuts import render

from rest_framework import mixins,viewsets,generics

from .serializers import ArtilclesSerializer,ArtilcleDetailSerializer, LabelsArticleSerializer, LabelsSerializer, HomeDataSerializer, CreateArtilcleSerializer, BlogImageSerializer, TaskSerializer
from .models import Label,Artilcle,HomeData,BlogImage,Task,TaskImage
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .filters import ArticleFilter
# Create your views here.

class ArticlesPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100


class ArticlesListViewSet(mixins.ListModelMixin,mixins.CreateModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    """
    商品列表页, 分页， 搜索， 过滤， 排序
    """
    queryset = Artilcle.objects.all().order_by('-add_time')
    # serializer_class = ArtilcleSerializer
    pagination_class = ArticlesPagination
    filter_backends = (DjangoFilterBackend,filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('title')
    ordering_fields = ('add_time',)
    filter_class = ArticleFilter
    def get_serializer_class(self):
        if self.action == "list":
            return ArtilclesSerializer
        elif self.action == "create":
            return CreateArtilcleSerializer
        else:
            return ArtilcleDetailSerializer


class HomeArticlesListViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):
    """
    首页文章
    """
    queryset = HomeData.objects.all()
    serializer_class = HomeDataSerializer


class AllLabelsViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    """
    list

    """
    queryset = Label.objects.all()
    pagination_class = ArticlesPagination
    def get_serializer_class(self):
        if self.action == "list":
            return LabelsSerializer
        elif self.action == "retrieve":
            return LabelsArticleSerializer


class BlogImageUploadSet(mixins.CreateModelMixin,viewsets.GenericViewSet):
    """
    首页文章
    """
    queryset = BlogImage.objects.all()
    serializer_class = BlogImageSerializer


class TaskUploadSet(mixins.CreateModelMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,viewsets.GenericViewSet):
    """
    上传多张图片接口
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

