from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.views.generic.edit import FormView
from django.views.generic import ListView
from post.models import Post
from user.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.


def home(request):
    return render(request, 'home.html', {'email': request.session.get('user')})


class Register(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/'


class Login(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):  # 유효성 검사가 끝났을 때, 즉 모든 데이터가 정상적일 때 실행
        self.request.session['user'] = form.email

        return super().form_valid(form)


def logout(request):
    if 'user' in request.session:
        del(request.session['user'])

    return redirect('/')


@method_decorator(login_required, name='dispatch')
class MyPage(ListView):  # 사용자가 지금까지 작성한 글을 보여주는 view
    template_name = 'mypage.html'

    # model을 지정하면 다른 사람들의 글도 볼 수 있기 때문에 문제가 될 수 있다.
    # 그래서 queryset을 사용
    # queryset을 만들 때 session에 접근이 필요하기 때문에 get_queryset을 사용한다
    def get_queryset(self, **kwargs):
        queryset = Post.objects.filter(
            user__email=self.request.session.get('user'))
        return queryset
