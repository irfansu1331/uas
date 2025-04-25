from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Alumni
from .forms import AlumniForm
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect

def home(request):
    return render(request, 'alumni_management/home.html')

class AlumniListView(UserPassesTestMixin, ListView):
    model = Alumni
    template_name = 'alumni_management/alumni_list.html'
    context_object_name = 'alumni'

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_admin

class AlumniDetailView(DetailView):
    model = Alumni
    template_name = 'alumni_management/alumni_detail.html'
    context_object_name = 'alumni'

    def get_queryset(self):
        user = self.request.user
        if user.is_admin:
            return Alumni.objects.all()
        else:
            return Alumni.objects.filter(user=user)

    
class AlumniCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Alumni
    form_class = AlumniForm
    template_name = 'alumni_management/alumni_form.html'

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_member or self.request.user.is_admin)

    def dispatch(self, request, *args, **kwargs):
        if hasattr(request.user, 'alumni'):
            return redirect('my_profile')  # kalau sudah punya alumni, jangan isi lagi
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user  # ⬅️ WAJIB baris ini!
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('my_profile')


class AlumniUpdateView(UpdateView):
    model = Alumni
    fields = ['nama', 'email', 'graduation_year', 'major', 'job_position', 'company']
    template_name = 'alumni_management/alumni_form.html'
    success_url = reverse_lazy('alumni_list')

    def get_queryset(self):
        user = self.request.user
        if user.is_admin:
            return Alumni.objects.all()
        else:
            return Alumni.objects.filter(user=user)


class AlumniDeleteView(UserPassesTestMixin, DeleteView):
    model = Alumni
    template_name = 'alumni_management/alumni_confirm_delete.html'
    success_url = reverse_lazy('alumni_list')

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_admin

class MyProfileView(LoginRequiredMixin, UpdateView):
    model = Alumni
    fields = ['nama', 'email', 'graduation_year', 'major', 'job_position', 'company']
    template_name = 'alumni_management/alumni_form.html'  # pakai form yg sama

    def get_object(self, queryset=None):
        return self.request.user.alumni

    def get_success_url(self):
        return reverse_lazy('my_profile')
