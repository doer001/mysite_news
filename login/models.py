from django.db import models


class User(models.Model):
    gender = (
        ('male', '男'),
        ('female', '女'),
    )

    name = models.CharField('用户名', max_length=128, unique=True)
    password = models.CharField('密码', max_length=256)
    email = models.EmailField('邮箱', unique=True)
    sex = models.CharField('性别', max_length=32, choices=gender, default='男')
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = verbose_name = '用户'
