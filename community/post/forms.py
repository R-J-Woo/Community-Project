from django import forms
from .models import Post
from user.models import User


class RegisterForm(forms.Form):
    # 작성자의 경우에는 입력하는 값이 아닌, 로그인한 정보가 자동으로 전달되어야 한다

    title = forms.CharField(
        error_messages={
            'required': '제목을 입력해주세요.'
        }, max_length=64, label='제목'
    )
    contents = forms.CharField(
        error_messages={
            'required': '내용을 입력해주세요.'
        }, label='내용'
    )
