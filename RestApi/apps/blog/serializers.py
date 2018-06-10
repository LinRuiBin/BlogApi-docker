from rest_framework import serializers

from .models import Label, Artilcle, HomeData, BlogImage, Task, TaskImage
from django.db.models import Q


class LabelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = "__all__"

class ArtilcleDetailSerializer(serializers.ModelSerializer):
    label = LabelsSerializer(many=True)
    class Meta:
        model = Artilcle
        fields = "__all__"

class CreateArtilcleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artilcle
        fields = ('title', 'art_desc', 'art_type', 'is_origin', 'label', 'id')

class ArtilclesSerializer(serializers.ModelSerializer):
    label = LabelsSerializer(many=True)
    class Meta:
        model = Artilcle
        exclude = ('art_desc' ,)


class ArticlesForLabelSerializer(serializers.ModelSerializer):
    label = LabelsSerializer(many=True)
    class Meta:
        model = Artilcle
        exclude = ('art_desc',)


class LabelsArticleSerializer(serializers.ModelSerializer):
    articles = ArticlesForLabelSerializer(many=True)
    class Meta:
        model = Label
        fields = "__all__"


class HomeDataSerializer(serializers.ModelSerializer):
    codes = serializers.SerializerMethodField()
    shares = serializers.SerializerMethodField()

    def get_codes(self, obj):
        all_arts = Artilcle.objects.filter(is_home=True).filter(art_type=1)
        art_serializer = ArtilclesSerializer(all_arts , many=True , context={'request': self.context['request']})
        return art_serializer.data

    def get_shares(self, obj):
        all_arts = Artilcle.objects.filter(is_home=True).filter(art_type=2)
        art_serializer = ArtilclesSerializer(all_arts , many=True , context={'request': self.context['request']})
        return art_serializer.data

    class Meta:
        model = HomeData
        fields = ('codes','shares')



class BlogImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None , allow_empty_file=False , use_url=True)
    class Meta:
        model = BlogImage
        fields = "__all__"


class TaskImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None , allow_empty_file=False , use_url=True)
    class Meta:
        model = TaskImage
        fields = ('image',)


# 上传多张图片 重写create方法
class TaskSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField
    title = serializers.CharField(max_length=50)
    images = TaskImageSerializer(many=True)

    def create(self , validated_data):
        images_data = self.context.get('view').request.FILES
        task = Task.objects.create(title=validated_data.get('title' , 'no-title'))
        for image_data in images_data.values():
            TaskImage.objects.create(task=task , image=image_data)
        return task

    class Meta:
        model = Task
        fields = ('__all__')