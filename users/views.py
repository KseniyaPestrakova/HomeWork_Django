from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.core.mail import send_mail
from django.contrib.auth import login

from config.settings import EMAIL_HOST_USER
from .forms import UserRegisterForm


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        send_mail(subject='Добро пожаловать в наш сервис',
                  message='Спасибо, что зарегистрировались в нашем сервисе!',
                  from_email=EMAIL_HOST_USER,
                  recipient_list=[user.email])
        return super().form_valid(form)
