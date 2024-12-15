from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy


# Create your views here.
class LoginUser(auth_views.LoginView):
    form_class = AuthenticationForm
    template_name = 'account/login.html'

    def get_success_url(self):
        return reverse_lazy('researches')

def logout_user(request):
    logout(request)
    return redirect('login')
