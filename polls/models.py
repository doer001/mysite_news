from django.db import models


class Question(models.Model):  # 每个类都要继承models.Model类
    id = models.AutoField(primary_key=True)  # 可以不写，因为默认就自动创建
    question_text = models.CharField(verbose_name='问题', max_length=200)  # 每个字段都是Field类的一个实例
    pub_time = models.DateTimeField(verbose_name='时间')  # 普通字段的第一个参数都是verbose_name,是一个更友好的别名

    class Meta:  # 模型元数据，指的是“除了字段外的所有内容”，例如排序方式、数据库表名、人类可读的单数或者复数名等等。
        verbose_name_plural = verbose_name = '问题'   # 人类可读的单数或者复数名
        ordering = ['-pub_time']    # 排序方式

    def __str__(self):  # 在打印对象时显示一些我们指定的信息。
        return self.question_text


class Choice(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='问题')
    choice_text = models.CharField(verbose_name='选项', max_length=200)
    votes = models.IntegerField(verbose_name='票数', default=0)

    class Meta:
        verbose_name = verbose_name_plural = '选项'

    def __str__(self):
        return self.choice_text
