from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, View
from django.contrib.auth.views import LoginView, LogoutView
from .models import User
from .forms import RegisterForm, LoginForm
from django.contrib.auth import login
from django.views.generic import TemplateView

from django.urls import reverse

class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'usermanagement/register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)

        # redirect berdasarkan role
        if user.is_admin:
            return redirect('alumni_list')
        elif user.is_member:
            return redirect('alumni_create')
        else:
            return redirect('home')


class RegisterSuccessView(TemplateView):
    template_name = 'usermanagement/register_success.html'
    
class UserLoginView(LoginView):
    form_class = LoginForm
    template_name = 'usermanagement/login.html'

class UserLogoutView(LogoutView):
    template_name = 'usermanagement/logout.html'

