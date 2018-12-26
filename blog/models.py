from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):   # 文章类别
    id = models.AutoField(primary_key=True)
    name = models.CharField('类别', max_length=20, unique=True)

    class Meta:
        verbose_name_plural = verbose_name = '类别'

    def __str__(self):
        return self.name


class Tag(models.Model):    # 文章标签
    id = models.AutoField(primary_key=True)
    name = models.CharField('标签', max_length=20, unique=True)

    class Meta:
        verbose_name = verbose_name_plural = '标签'

    def __str__(self):
        return self.name


class Article(models.Model):    # 文章
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='作者')  # 什么也不做
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=1, verbose_name='类别')  # 将外键字段设为默认值
    tag = models.ManyToManyField(Tag, verbose_name='标签')
    title = models.CharField('标题', max_length=50)
    content = models.TextField('内容')
    pub_time = models.DateField('日期', auto_now=True)    # auto_now=True修改日期

    class Meta:
        verbose_name = verbose_name_plural = '文章'

    def __str__(self):
        return self.title


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='文章')  # 将定义有外键的模型对象同时删除
    reply = models.ForeignKey('self', on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name='回复')
    name = models.CharField('昵称', max_length=20)
    email = models.EmailField('邮箱')
    content = models.TextField('内容')
    publish = models.DateField('时间', auto_now_add=True)  # uto_now_add=True发布日期

    class Meta:
        verbose_name_plural = verbose_name = '评论'

    def __str__(self):
        return self.content
