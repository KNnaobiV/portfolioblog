from django.shortcuts import render, reverse, get_object_or_404
from django.views.generic import DetailView, ListView
from website.models import Post, Comment, Tag
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


class TagDetailView(ListView):
    model = Post
    context_object_name = 'tag'
    template_name = 'website/tag_detail.html'

    def get_queryset(self):
        tag = get_object_or_404(Tag, name=self.kwargs.get('name'))
        return Post.objects.filter(tag=tag)
