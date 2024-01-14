from django.urls import path

from blog.apps import BlogConfig
from blog.views import PostListView, PostCreateView

app_name = BlogConfig.name

urlpatterns = [
    path('list/', PostListView.as_view(), name='list'),
    path('create/', PostCreateView.as_view(), name='create'),
]
