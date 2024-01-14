from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from pytils.translit import slugify

from blog.models import Post


class PostListView(ListView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = ('title', 'text', 'preview_image', 'is_published')
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)
class PostDetailView(DetailView):
    model = Post


