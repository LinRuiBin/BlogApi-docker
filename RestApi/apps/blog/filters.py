import django_filters

from .models import Label,Artilcle
from django.db.models import Q


class ArticleFilter(django_filters.rest_framework.FilterSet):
    """
    商品的过滤类
    """
    title = django_filters.CharFilter(name='title', help_text="文章标题")

    class Meta:
        model = Artilcle
        fields = ['title']