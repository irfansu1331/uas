from django.urls import include, path

urlpatterns = [
    path('', include('alumni_app.urls')),
    path('about/', include('about.urls')),
    path('contacts/', include('contacts.urls')),
]
