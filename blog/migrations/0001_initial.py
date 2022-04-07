# Generated by Django 4.0.3 on 2022-03-30 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='タイトル')),
                ('content', models.TextField(verbose_name='本文')),
                ('posted_at', models.DateTimeField(auto_now_add=True, verbose_name='投稿日時')),
                ('category', models.CharField(choices=[('将棋', '将棋'), ('日常のこと', '日常のこと'), ('プログラミングについて', 'プログラミングについて')], max_length=50, verbose_name='カテゴリ')),
            ],
        ),
    ]
