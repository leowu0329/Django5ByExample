from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path(
        'accounts/profile/',
        login_required(
            TemplateView.as_view(template_name='accounts/profile.html')
        ),
        name='profile',
    ),
]
