# Generated by Django 2.0.1 on 2018-01-21 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awareness_blog', '0002_auto_20180121_0535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='teaser',
            field=models.TextField(),
        ),
    ]
