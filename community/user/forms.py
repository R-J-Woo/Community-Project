from django.db import IntegrityError
from django.forms import Form, PasswordInput
from django import forms
from django.contrib.auth.hashers import check_password, make_password
from .models import User


class RegisterForm(forms.Form):
    email = forms.EmailField(
        error_messages={
            'required': '이메일을 입력해주세요.'
        }, max_length=64, label='이메일'
    )
    password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요.'
        }, widget=forms.PasswordInput, label='비밀번호'
    )
    re_password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요.'
        }, widget=forms.PasswordInput, label='비밀번호 확인'
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')

        if email and password and re_password:
            if password != re_password:
                self.add_error('password', '비밀번호가 서로 다릅니다')
                self.add_error('re_password', '비밀번호가 서로 다릅니다')
            else:
                try:  # email이 존재하고 있을 때 error처리
                    user = User(
                        email=email,
                        password=make_password(password)
                    )
                    user.save()
                except IntegrityError:
                    self.add_error('email', '이메일이 이미 존재합니다.')


class LoginForm(forms.Form):
    email = forms.EmailField(
        error_messages={
            'required': '이메일을 입력해주세요.'
        }, max_length=64, label='이메일'
    )
    password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요.'
        }, widget=forms.PasswordInput, label='비밀번호'
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            try:  # 입력한 이메일로 사용자가 있는지 확인
                user = User.objects.get(email=email)
            except User.DoesNotExist:  # 입력한 이메일에 대한 사용자가 없으면
                self.add_error('email', '아이디가 없습니다.')
                return

            if not check_password(password, user.password):  # 비밀번호가 틀렸으면
                self.add_error('password', '비밀번호가 틀렸습니다.')
            else:  # 비밀번호가 맞았으면
                self.email = user.email
