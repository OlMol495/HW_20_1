from django.urls import path

from blog.apps import BlogConfig
from blog.views import PostListView

app_name = BlogConfig.name

urlpatterns = [
    path('list/', PostListView.as_view(), name='list'),
]
