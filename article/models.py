from django.db import models
from django.contrib.auth.models import User
import time


class Category(models.Model):
    name = models.CharField("名称", max_length=64)
    create_time = models.DateTimeField("添加时间", auto_now_add=True)
    status = models.IntegerField("状态", default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "文章分类"
        verbose_name_plural = "文章分类"


def upload_to_goods_img(instance, filename):
    return 'article/{prefix}_{filename}.{suffix}'.format(prefix='article',
                filename=int(time.time() * 1000),
                suffix=filename.split('.')[-1])


class Article(models.Model):
    category = models.ForeignKey(Category, verbose_name='分类')
    user = models.ForeignKey(User)
    title = models.CharField("标题", max_length=128)
    description = models.CharField("描述", max_length=256)
    article = models.TextField("文章")
    create_time = models.DateTimeField("发表时间", auto_now_add=True)
    status = models.IntegerField('状态', default=0)
    img = models.ImageField("图片", upload_to=upload_to_goods_img)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "文章信息"
        verbose_name_plural = "文章信息"



