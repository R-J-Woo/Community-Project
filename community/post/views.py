from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from user.decorators import login_required
from .models import Post
from .forms import RegisterForm
from user.models import User
from comment.models import Comment
from comment.forms import RegisterForm as CommentForm
from django.utils.decorators import method_decorator
from django.contrib import messages
# Create your views here.


class PostList(ListView):  # post 목록을 보여주는 view
    model = Post
    template_name = 'board.html'


@login_required
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


@method_decorator(login_required, name='dispatch')
class PostDetail(DetailView):  # 글 상세보기 view
    template_name = 'post_detail.html'
    queryset = Post.objects.all()
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm(self.request)
        context['comments'] = Comment.objects.filter(post=self.kwargs['pk'])
        return context


@login_required
def PostUpdate(request, pk):
    post = Post.objects.get(id=pk)
    if post.user != request.user:  # 글 작성자가 아니면 글을 수정할 수 없도록 함
        return redirect('/board/')

    if request.method == 'POST':
        form = RegisterForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('/board/')
    else:
        form = RegisterForm(instance=post)
    return render(request, 'post_update.html', {'form': form})


@login_required
def PostDelete(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect('/board/')
