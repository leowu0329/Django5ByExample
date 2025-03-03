from django.shortcuts import redirect, render
from django.contrib import messages
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from allauth.account.adapter import get_adapter
from allauth.account.models import EmailAddress
from allauth.account.utils import send_email_confirmation
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

User = get_user_model()

@require_http_methods(["POST"])
def resend_verification(request):
    email = request.POST.get("email")
    if not email:
        messages.error(request, "請提供有效的電子郵件地址。")
        return redirect("account_email_verification_sent")

    try:
        # 查找與此郵件關聯的 EmailAddress 對象
        email_address = EmailAddress.objects.get(email=email)
        user = email_address.user

        if email_address.verified:
            messages.error(request, "此電子郵件地址已經驗證過了。")
        else:
            # 重新發送驗證郵件
            try:
                send_email_confirmation(request, user, email=email)
                messages.success(request, "驗證碼已重新發送，請檢查您的郵件。")
            except Exception as e:
                messages.error(request, "發送驗證碼時發生錯誤，請稍後再試。")

    except EmailAddress.DoesNotExist:
        messages.error(request, "找不到此電子郵件地址的註冊信息。")

    return redirect("account_email_verification_sent")

@require_http_methods(["POST"])
def resend_login_verification(request):
    email = request.POST.get("email")
    if not email:
        messages.error(request, "請提供有效的電子郵件地址。")
        return redirect("account_confirm_login_code")

    try:
        # 查找與此郵件關聯的 EmailAddress 對象
        email_address = EmailAddress.objects.get(email=email)
        user = email_address.user

        # 重新發送驗證郵件
        try:
            send_email_confirmation(request, user, email=email)
            messages.success(request, "登入驗證碼已重新發送，請檢查您的郵件。")
        except Exception as e:
            messages.error(request, "發送驗證碼時發生錯誤，請稍後再試。")

    except EmailAddress.DoesNotExist:
        messages.error(request, "找不到此電子郵件地址的註冊信息。")

    return redirect("account_confirm_login_code")

@login_required
def index(request):
    return render(request, 'index.html') 