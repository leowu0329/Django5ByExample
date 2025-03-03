import dj_database_url
from pathlib import Path
from environ import Env

env=Env()
Env.read_env()

ENVIRONMENT = env('ENVIRONMENT',default="production")

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = env('SECRET_KEY')

if ENVIRONMENT == 'development':
    DEBUG = True
else:
    DEBUG = False

ALLOWED_HOSTS = ['*','https://django5byexample.onrender.com']

CSRF_TRUSTED_ORIGINS = ['https://django5byexample.onrender.com']

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    'cloudinary_storage',
    'cloudinary',
    "django.contrib.staticfiles",
    'allauth',
    'allauth.account',
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = "src.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR/"templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "src.wsgi.application"

if ENVIRONMENT == 'development':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': dj_database_url.parse(env('DATABASE_URL'))
    }


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "zh-hant"
TIME_ZONE = "Asia/Taipei"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
STATICFILES_DIRS = [ BASE_DIR / 'static' ]
STATIC_ROOT=BASE_DIR /'staticfiles'
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticCloudinaryStorage'


MEDIA_URL = 'media/'

if ENVIRONMENT == 'development':
    MEDIA_ROOT = BASE_DIR / 'media' 
else:
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
    CLOUDINARY_STORAGE={
        'CLOUDINARY_URL': env('CLOUDINARY_URL')
    }

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

SITE_ID = 1

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='smtp.gmail.com'
EMAIL_HOST_USER=env('EMAIL_ADDRESS')
EMAIL_HOST_PASSWORD=env('EMAIL_HOST_PASSWORD')
EMAIL_PORT=587
EMAIL_USE_TLS=True
DEFAULT_FROM_EMAIL=f"Django App Name {env('EMAIL_ADDRESS')}"
ACCOUNT_EMAIL_SUBJECT_PREFIX=''

# 電子郵件驗證設定
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3
ACCOUNT_CONFIRM_EMAIL_ON_GET = True  # 允許通過 GET 請求確認郵件

# 驗證後重定向設定
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = False  # 驗證成功後不自動登入
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = "/accounts/login/"  # 驗證後跳轉到登入頁
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = "/accounts/login/"      # 驗證後跳轉到登入頁

# 登入相關設定
ACCOUNT_RATE_LIMITS = {
    'login_failed': '5/300s',  # 5次失敗後，等待300秒
    'send_mail': '3/3600s',    # 每小時最多發送3次郵件
    'reset_password': '3/3600s',  # 每小時最多重設3次密碼
    'confirm_email': '3/180s',  # 每180秒最多發送3次確認郵件
}
ACCOUNT_LOGIN_ON_PASSWORD_RESET = False  # 重設密碼後不自動登入

# 註冊相關設定
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True  # 註冊時需要輸入兩次密碼
ACCOUNT_USERNAME_MIN_LENGTH = 3  # 用戶名最小長度
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = False  # 註冊時不需要輸入兩次郵箱
ACCOUNT_PRESERVE_USERNAME_CASING = False  # 用戶名不區分大小寫
ACCOUNT_USERNAME_BLACKLIST = []  # 禁止使用的用戶名列表
ACCOUNT_SIGNUP_REDIRECT_URL = "/accounts/email-verification-sent/"  # 註冊後跳轉到驗證郵件發送頁面

# 登入方法設定
ACCOUNT_LOGIN_METHODS = {'username', 'email'}  # 允許使用用戶名或郵箱登入

# 登入重定向設定
LOGIN_URL = '/accounts/login/'  # 未登入時跳轉到登入頁面
LOGIN_REDIRECT_URL = '/'  # 登入成功後跳轉到首頁
LOGOUT_REDIRECT_URL = '/accounts/login/'  # 登出後跳轉到登入頁面
ACCOUNT_LOGOUT_REDIRECT_URL = '/accounts/login/'  # django-allauth 登出後跳轉到登入頁面

# 會話設定
ACCOUNT_SESSION_REMEMBER = True  # 記住登入狀態
SESSION_COOKIE_AGE = 60 * 60 * 24 * 30  # 30天
SESSION_COOKIE_SECURE = True  # 只在 HTTPS 下發送 Cookie

# 其他設定
ACCOUNT_LOGOUT_ON_GET = False  # 禁止通過 GET 請求登出
ACCOUNT_USER_MODEL_USERNAME_FIELD = 'username'  # 用戶名欄位
ACCOUNT_EMAIL_SUBJECT_PREFIX = ''  # 郵件主題前綴

# Debug 設定
if ENVIRONMENT == 'development':
    # EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # 開發環境下在控制台輸出郵件
    SESSION_COOKIE_SECURE = False  # 開發環境允許非 HTTPS
