from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from .views import resend_verification, resend_login_verification, index

urlpatterns = [
    path("", index, name="index"),
    path("admin/", admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path(
        'accounts/profile/',
        login_required(
            TemplateView.as_view(template_name='account/profile.html')
        ),
        name='profile',
    ),
    path('accounts/resend-verification/', resend_verification, name='resend_verification'),
    path('accounts/resend-login-verification/', resend_login_verification, name='resend_login_verification'),
]
