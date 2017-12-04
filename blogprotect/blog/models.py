from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible


# Create your models here.
class Category(models.Model):
    # 博客名字，博客类
    name = models.CharField(max_length=100 ,verbose_name='博客名字')

    def __str__(self):
        return self.name


class Tag(models.Model):  # 博客的个人标签
    # 标签
    name = models.CharField(max_length=100,verbose_name='标签')

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Post(models.Model):
    # 文章的数据
    # 文章标题
    title = models.CharField(max_length=70,verbose_name='标题')
    # 文章正文
    body = models.TextField(verbose_name='正文')
    # 文章的创建时间和修改时间
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    # 文章摘要
    excerpt = models.CharField(max_length=200, blank=True,verbose_name='摘要')
    #  分类于标签
    category = models.ForeignKey(Category,verbose_name='标签')
    tags = models.ManyToManyField(Tag, blank=True)  # 和标签为多对多关系
    # 作者 这里使用的use 是django自己携带的用户类型
    author = models.ForeignKey(User)

    def __str__(self):
        return self.title

    # 自定义get_absolute_url方法 更好获取url的值
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})
    class Meta:
        ordering = ['-created_time']