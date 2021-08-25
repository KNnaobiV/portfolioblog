from django.urls import path
from website.views import PostListView, PostDetailView, TagListView

app_name = 'website'

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('detail/<int:pk>/<slug>/', PostDetailView.as_view(), name='post-detail'),
    path('tag/<slug>/', TagListView.as_view, name='tag_list'),
]
