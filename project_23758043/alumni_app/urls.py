from django.urls import path
from .views import (home, AlumniListView, AlumniDetailView, AlumniCreateView, AlumniUpdateView, AlumniDeleteView, MyProfileView)

urlpatterns = [
    path('', home, name='home'),
    path('alumni/', AlumniListView.as_view(), name='alumni_list'),
    path('alumni/create/', AlumniCreateView.as_view(), name='alumni_create'),
    path('alumni/<int:pk>/detail/', AlumniDetailView.as_view(), name='alumni_detail'),  # <-- tambahkan ini
    path('alumni/<int:pk>/update/', AlumniUpdateView.as_view(), name='alumni_update'),
    path('alumni/<int:pk>/delete/', AlumniDeleteView.as_view(), name='alumni_delete'),
    path('profile/', MyProfileView.as_view(), name='my_profile'),
]
