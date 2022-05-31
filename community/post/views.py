from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.views.generic.edit import FormView
from .models import Post
from .forms import RegisterForm
from user.models import User
# Create your views here.


class PostList(ListView):  # post 목록을 보여주는 view
    model = Post
    template_name = 'board.html'


# class PostRegister(FormView): # post 등록하는 view
#     form_class = RegisterForm
#     template_name = 'post_register.html'

#     def get_context_data(self, **kwargs):  # get_context_date는 template에 원하는 것을 보낼 수 있다
#         context = super().get_context_data(**kwargs)
#         context['request'] = self.request
#         return context

#     def get_form_kwargs(self, **kwargs):
#         kw = super().get_form_kwargs(**kwargs)

def PostRegister(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user_email = request.session.get('user')  # 작성자의 이메일을 가져옴
            user = User.objects.get(email=user_email)  # 그 이메일에 해당하는 사용자를 가져옴

            post = Post(
                user=user,
                title=form.cleaned_data['title'],
                contents=form.cleaned_data['contents']
            )
            post.save()

            return redirect('/board/')

    else:
        form = RegisterForm()

    return render(request, 'post_register.html', {'form': form})
