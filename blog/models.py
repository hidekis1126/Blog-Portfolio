from tabnanny import verbose
from django.db import models


class BlogPost(models.Model):
    CATEGORY = (('将棋', '将棋'), ('日常のこと', '日常のこと'), ('プログラミングについて', 'プログラミングについて'))
    title = models.CharField(verbose_name='タイトル', max_length=200)
    image = models.ImageField(upload_to='images', verbose_name='イメージ画像', null=True, blank=True)
    content = models.TextField(verbose_name='本文')
    posted_at = models.DateTimeField(verbose_name='投稿日時', auto_now_add=True)
    category = models.CharField(verbose_name='カテゴリ', max_length=50, choices=CATEGORY)

    def __str__(self):
        return self.title