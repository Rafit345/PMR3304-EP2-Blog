from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import generic

from .models import Post, Comment
from .forms import PostForm, CommentForm


class PostListView(generic.ListView):
    model = Post
    template_name = 'posts/index.html'


class PostDetailView(generic.DetailView):
    # responde com 404 automaticamente se o post não existir
    model = Post
    template_name = 'posts/detail.html'

    # comentários do post, do mais recente para o mais antigo
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_list'] = self.object.comment_set.order_by('-date')
        return context


class PostCreateView(generic.CreateView):
    model = Post
    template_name = 'posts/create.html'
    form_class = PostForm

    # após criar, redireciona para a página do post
    def get_success_url(self):
        return reverse('posts:detail', args=(self.object.id, ))


class PostUpdateView(generic.UpdateView):
    model = Post
    template_name = 'posts/update.html'
    form_class = PostForm

    def get_success_url(self):
        return reverse('posts:detail', args=(self.object.id, ))


class PostDeleteView(generic.DeleteView):
    # GET exibe a página de confirmação; POST apaga o post
    model = Post
    template_name = 'posts/delete.html'
    success_url = reverse_lazy('posts:index')


def create_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_author = form.cleaned_data['author']
            comment_text = form.cleaned_data['text']
            comment = Comment(author=comment_author,
                              text=comment_text,
                              post=post)
            comment.save()
            return HttpResponseRedirect(
                reverse('posts:detail', args=(post_id, )))
    else:
        form = CommentForm()
    context = {'form': form, 'post': post}
    return render(request, 'posts/comment.html', context)
