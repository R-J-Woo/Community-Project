from distutils.log import error
from django import forms
from .models import Comment
from user.models import User
from post.models import Post


class RegisterForm(forms.Form):
    # 작성자의 경우에는 입력하는 값이 아닌, 로그인한 정보가 자동으로 전달되어야 한다
    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    # post는 post의 id로 받을 것이기 때문에 IntegerField를 사용한다
    post = forms.IntegerField(
        widget=forms.HiddenInput
    )
    comment = forms.CharField(
        error_messages={
            'required': '댓글을 입력해주세요.'
        }, label='댓글 작성하기'
    )

    def clean(self):
        cleaned_data = super().clean()
        post = cleaned_data.get('post')
        comment = cleaned_data.get('comment')
        user = self.request.session.get('user')

        if post and comment and user:
            comment = Comment(
                post=Post.objects.get(pk=post),
                comment=comment,
                user=User.objects.get(email=user)
            )
            comment.save()
        else:
            self.post = post
            self.add_error('comment', '댓글이 입력되지 않았습니다.')
