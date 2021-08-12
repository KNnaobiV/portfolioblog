from django.forms import ModelForm
from website.models import Comment

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'email', 'body']
