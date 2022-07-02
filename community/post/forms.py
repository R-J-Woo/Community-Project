from django import forms
from .models import Post
from user.models import User


class RegisterForm(forms.ModelForm):
    # 작성자의 경우에는 입력하는 값이 아닌, 로그인한 정보가 자동으로 전달되어야 한다
    class Meta:
        model = Post
        fields = ['title', 'contents']
