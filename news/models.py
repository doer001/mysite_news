from django.db import models
from django.urls import reverse


class User(models.Model):
    name = models.CharField('作者', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = '作者'


class Column(models.Model):
    name = models.CharField('栏目名称', max_length=256)
    slug = models.CharField('栏目网址', max_length=256, db_index=True)
    intro = models.TextField('栏目简介', default='')

    def get_url(self):
        return reverse('news:column', args=(self.slug,))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = '栏目'
        ordering = ['name']  # 按照哪个栏目排序


class Article(models.Model):
    column = models.ManyToManyField(Column, verbose_name='归属栏目')

    title = models.CharField('标题', max_length=256)
    slug = models.CharField('网址', max_length=256)

    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='作者')
    content = models.TextField('内容', default='', blank=True)

    published = models.BooleanField('正式发布', default=True)
    pub_date = models.DateField('发表时间', auto_now_add=True, editable=True)
    update_date = models.DateField('更改时间', auto_now=True, null=True)

    def get_url(self):
        return reverse('news:article', args=(self.pk,))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = verbose_name_plural = '教程'
