# Generated by Django 2.0.1 on 2018-01-22 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('zip_code', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='feedback',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedback.School'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='user_email',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedback.User'),
        ),
    ]
