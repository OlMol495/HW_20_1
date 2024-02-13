from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db import transaction
from django.forms import inlineformset_factory
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView

from catalog.forms import ProductForm, VersionForm, ModeratorProductForm
from catalog.models import Product, Contact, Category, Version


class HomeTemplateView(TemplateView):
    """
    Обработка запроса на отображение главной страницы
    """
    template_name = 'catalog/home.html'
    extra_context = {'title': 'Best Store Ever'}

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Product.objects.all()[:3]
        return context_data


class ProductListView(ListView):
    """
    Обработка запросов на отображение списка товаров
    """
    model = Product
    extra_context = {'title': 'Каталог продуктов'}
    paginate_by = 4


class ProductDetailView(DetailView):
    """
    Обработка запросов для отображения информации по конкретному товару
    """
    model = Product
    extra_context = {'title': 'Детальная информация о товаре'}


class ProductCreateView(LoginRequiredMixin, CreateView):
    """
    Обработка запросов для создания товара
    """
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:catalog')

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()

        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """
    Обработка запросов для редактирования товара
    """
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:catalog')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        if formset is None:
            return super().form_valid(form)
        with transaction.atomic():
            if form.is_valid():
                self.object = form.save()
                if formset.is_valid():
                    formset.instance = self.object
                    formset.save()
                else:
                    return self.form_invalid(form)

        return super().form_valid(form)

    def get_form_class(self):
        """
        Проверка прав пользователя на редактирования товара
        """
        if self.request.user == self.object.owner:
            return ProductForm
        elif self.request.user.groups.filter(name='moderator'):
            return ModeratorProductForm
        else:
            raise Http404('Только владелец товара может вносить изменения')


def contacts(request):
    company_info = Contact.objects.all()
    info_content = {
        'info_list': company_info,
        'title': 'Контакты'
    }
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f"{name} ({phone}): {message}")
    return render(request, "catalog/contacts.html", info_content)
