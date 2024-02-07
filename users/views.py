from django.contrib import messages
from django.shortcuts import redirect
from config import settings
from random import randint
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.views import PasswordResetView
from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, FormView
from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        self.object = form.save()
        send_mail(
            subject='Поздравляем с регистрацией',
            message=f'Вы успешно прошли регистрацию в BestStoreEver',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.object.email]
        )
        return super().form_valid(form)


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


def generate_new_password(request):
    new_password = User.objects.make_random_password()
    request.user.set_password(new_password)
    request.user.save()
    send_mail(
        subject='Смена пароля в BestStoreEver',
        message=f'Ваш новый пароль для BestStoreEver: {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )
    messages.success(request, 'Вам на почту отправлено письмо с новым паролем')
    return redirect(reverse('catalog:home'))


# class CustomPasswordResetView(PasswordResetView):
#
#     def form_valid(self, form):
#         new_password = ''.join([str(randint(0, 9)) for _ in range(10)])
#         #new_password = self.User.objects.make_random_password()
#         email = form.cleaned_data['email']
#         User = get_user_model()
#         user = User.objects.get(email=email)
#         user.set_password(new_password)
#         user.save()
#         send_mail(
#             subject='Восстановление пароля',
#             message=f'Ваш новый пароль: {new_password}',
#             from_email=settings.EMAIL_HOST_USER,
#             recipient_list=[user.email]
#         )
#         return super().form_valid(form)








        # email = form.cleaned_data['email']
        # user = User.objects.get(email=email)
        # uid = urlsafe_base64_encode(force_bytes(user.pk))
        # token = default_token_generator.make_token(user)
        # reset_url = reverse('password_reset_confirm', kwargs={'idb64': uid, 'token': token})

