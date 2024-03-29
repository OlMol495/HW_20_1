from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify
from blog.models import Post
from config.settings import EMAIL_HOST_USER


class PostListView(ListView):
    model = Post
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_published=True)
        return queryset



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

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views += 1
        self.object.save()
        if self.object.views == 100:
            send_mail(subject="Hi there!", message="You got 100 views!", from_email=EMAIL_HOST_USER,
                      recipient_list=[EMAIL_HOST_USER])
        return self.object

class PostUpdateView(UpdateView):
    model = Post
    fields = ('title', 'text', 'preview_image', 'is_published')
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("blog:detail", args=[self.kwargs.get('pk')])


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:list')

