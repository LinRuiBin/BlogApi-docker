from rest_framework import serializers

from .models import Goods,GoodsCategory,GoodsImage



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsImage
        fields = ("image", )


class GoodsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    images = GoodsImageSerializer(many=True)
    class Meta:
        model = Goods
        fields = "__all__"



class GoodCategorySerializer3(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodCategorySerializer2(serializers.ModelSerializer):
    sub_cat = GoodCategorySerializer3(many=True)
    class Meta:
        model = GoodsCategory
        fields = "__all__"

class GoodCategorySerializer(serializers.ModelSerializer):
    """
    商品类别序列化
    """
    # parent_category = ''
    sub_cat = GoodCategorySerializer2(many=True)
    class Meta:
        model = GoodsCategory
        fields = "__all__"