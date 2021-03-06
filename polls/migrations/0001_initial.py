# Generated by Django 2.0.4 on 2018-12-25 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('choice_text', models.CharField(max_length=200, verbose_name='选项')),
                ('votes', models.IntegerField(default=0, verbose_name='票数')),
            ],
            options={
                'verbose_name': '选项',
                'verbose_name_plural': '选项',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('question_text', models.CharField(max_length=200, verbose_name='问题')),
                ('pub_time', models.DateTimeField(verbose_name='时间')),
            ],
            options={
                'verbose_name': '问题',
                'verbose_name_plural': '问题',
                'ordering': ['-pub_time'],
            },
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Question', verbose_name='问题'),
        ),
    ]
