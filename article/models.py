from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
import time
from DjangoUeditor.models import UEditorField
from DjangoUeditor.widgets import UEditorWidget


class Category(models.Model):
    """
     状态类别
     """
    CATEGORY_TYPE = (
        (0, "启用"),
        (1, "关闭"),

    )
    name = models.CharField("名称", max_length=64)
    create_time = models.DateTimeField("添加时间", auto_now_add=True)
    status = models.IntegerField("状态", choices=CATEGORY_TYPE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "文章分类"
        verbose_name_plural = "文章分类"


def upload_to_goods_img(instance, filename):
    date = datetime.datetime.now()
    format_ = "%Y-%m-%d %H:%M:%S"
    date_str = date.strftime(format_)  # 格式化时间
    today_str = f"{str(date_str).split(' ')[0]} 00:00:00"   # 时间转成字符串
    return 'article/{today_str}/{prefix}_{filename}.{suffix}'.format(today_str=today_str,
                                                                     prefix='article',
                                                                     filename=int(time.time() * 1000),
                                                                     suffix=filename.split('.')[-1])


class Article(models.Model):
    CATEGORY_TYPE = (
        (0, "显示"),
        (1, "禁用"),

    )
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE, verbose_name='分类')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="作者")
    title = models.CharField("标题", max_length=128)
    description = models.CharField("描述", max_length=256)
    article = UEditorField(verbose_name='内容详情', width=600, height=300, toolbars="full", imagePath=upload_to_goods_img,
                           filePath="course/ueditor/", upload_settings={"imageMaxSize":1204000},default='')
    create_time = models.DateTimeField("发表时间", auto_now_add=True)
    status = models.IntegerField('状态', choices=CATEGORY_TYPE)
    title_img = models.ImageField("图片", upload_to=upload_to_goods_img, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "文章信息"
        verbose_name_plural = "文章信息"


