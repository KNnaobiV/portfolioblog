from django.shortcuts import render, reverse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from website.models import Post, Tag, Comment
from django.views.generic.edit import FormMixin
from website.forms import CommentForm
# Create your views here.

class PostListView(ListView):
    model = Post
    paginate_by = 5
    context_object_name = 'posts'

class PostDetailView(DetailView, FormMixin):
    model = Post
    context_object_name = 'post'
    form_class = CommentForm

    def get_success_url(self):
        return reverse('website:post-detail',
            kwargs={'slug': self.object.slug, 'pk': self.object.pk})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form.invalid(form)

    def form_valid(self, form):
        form.instance.post = Post.objects.get(pk=self.kwargs.get('pk'))
        form.save()
        return super(PostDetailView, self).form_valid(form)
