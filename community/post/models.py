from django.db import models

# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(
        'user.User', on_delete=models.CASCADE, verbose_name='작성자')
    title = models.CharField(max_length=64, verbose_name='제목')
    contents = models.TextField(verbose_name='내용')
    register_date = models.DateTimeField(
        auto_now_add=True, verbose_name='등록날짜')
