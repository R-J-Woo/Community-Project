from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from .forms import RegisterForm
from user.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.


@method_decorator(login_required, name='dispatch')
class CommentCreate(FormView):  # 댓글 생성하는 view
    form_class = RegisterForm
    success_url = '/board/'

    def form_invalid(self, form):  # 댓글 작성에 실패했을 경우에 실행
        return redirect('/board/' + str(form.post))

    def get_form_kwargs(self, **kwargs):
        kw = super().get_form_kwargs(**kwargs)
        kw.update({
            'request': self.request
        })
        return kw
