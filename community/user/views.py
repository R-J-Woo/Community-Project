from django.shortcuts import render
from .forms import RegisterForm, LoginForm
from django.views.generic.edit import FormView
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
