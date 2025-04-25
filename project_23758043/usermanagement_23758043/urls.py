from django.urls import path
from .views import RegisterView, TemplateView, UserLoginView, UserLogoutView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('register/success/', TemplateView.as_view(template_name='usermanagement/register_success.html'), name='register_success'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]
