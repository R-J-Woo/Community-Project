from django.db import models

# Create your models here.


class Comment(models.Model):
    post = models.ForeignKey(  # 어떤 글에 댓글을 달았는지
        'post.Post', on_delete=models.CASCADE, verbose_name='글')
    user = models.ForeignKey(  # 댓글 작성한 사람
        'user.User', on_delete=models.CASCADE, verbose_name='작성자')
    comment = models.TextField(verbose_name='댓글')
    register_date = models.DateTimeField(
        auto_now_add=True, verbose_name='등록날짜')
