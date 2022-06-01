from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from .models import Post
from .forms import RegisterForm
from user.models import User
from comment.models import Comment
from comment.forms import RegisterForm as CommentForm
# Create your views here.


class PostList(ListView):  # post 목록을 보여주는 view
    model = Post
    template_name = 'board.html'


def PostRegister(request):  # post를 작성하여 등록하는 view
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


class PostDetail(DetailView):  # 글 상세보기 view
    template_name = 'post_detail.html'
    queryset = Post.objects.all()
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm(self.request)
        context['comments'] = Comment.objects.filter(post=self.kwargs['pk'])
        return context
