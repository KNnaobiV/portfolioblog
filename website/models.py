from django.db import models
from django.utils import timezone
from django.shortcuts import reverse
# Create your models here.

class Post(models.Model):
    STATUS = (('draft', 'DRAFT'), ('published', 'PUBLISHED'))
    title = models.CharField(max_length=255)
    body = models.TextField()
    slug = models.SlugField()
    published_status = models.CharField(choices=STATUS, default='draft',
     max_length=10)
    published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('website:post-detail', args=[self.pk, self.slug])


class Comment(models.Model):
    STATUS = (('true', 'TRUE'), ('false', 'FALSE'),)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, 
    related_name='comment')
    author = models.CharField(max_length=100, default='anonymous')
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    published_status = models.CharField(max_length=6, choices=STATUS,
     default='FALSE')

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'


class Tag(models.Model):
    post = models.ManyToManyField(Post)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
    #implementation for all the post with particular tag
