from django.db import models
from datetime import datetime
from DjangoUeditor.models import UEditorField
# Create your models here.

class Label(models.Model):
    name = models.CharField(max_length=10 , verbose_name="文章标签")

    class Meta:
        verbose_name = "文章标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Artilcle(models.Model):
    """
    商品类别
    """
    TYPE = (
        (1 , "编程") ,
        (2 , "生活") ,
    )

    title = models.CharField(max_length=50 , verbose_name="文章标题")
    art_desc = models.TextField(verbose_name=u"内容", max_length=10000)
    art_type = models.IntegerField(choices=TYPE , verbose_name="文章分类" , help_text="分类")
    add_time = models.DateTimeField(default=datetime.now , verbose_name="发布时间")
    is_origin = models.BooleanField(default=True , verbose_name="是否原创")
    # label = models.ForeinKey(Label, verbose_name="文章标签" , related_name='articles')
    label = models.ManyToManyField(Label, verbose_name="文章标签" , related_name='articles')
    is_home = models.BooleanField(default=False , verbose_name="是否在首页显示")
    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name
        db_table = "blog_article"

    def __str__(self):
        return self.title

class HomeData(models.Model):
    codes = models.CharField(max_length=50 , verbose_name="首页codes")
    shares = models.CharField(max_length=50 , verbose_name="首页shares")
    name = models.CharField(max_length=50 , verbose_name="名字" ,default="首页数据")

    class Meta:
        verbose_name = "首页数据"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class BlogImage(models.Model):
    # name = models.CharField(max_length=50 , verbose_name="图片描述")
    image = models.ImageField(upload_to="blogs/images/%Y/%m" , null=True , blank=True , verbose_name="博客图片")

    class Meta:
        verbose_name = "博客图片"
        verbose_name_plural = verbose_name


class Task(models.Model):
    title = models.CharField(max_length=50 , verbose_name="测试标题")


class TaskImage(models.Model):
    # name = models.CharField(max_length=50 , verbose_name="图片描述")
    image = models.ImageField(upload_to="testimg/images/%Y/%m" , null=True , blank=True , verbose_name="测试图片")
    task = models.ForeignKey(Task, verbose_name="测试模型" , related_name='images')

    class Meta:
        verbose_name = "测试图片"
        verbose_name_plural = verbose_name