"""
Configurações base do projeto — compartilhadas entre todos os ambientes.
As configurações específicas de cada ambiente ficam em local.py / production.py
"""

from pathlib import Path
from decouple import config

# Raiz do projeto: dois níveis acima de config/settings/
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# ─── Segurança ────────────────────────────────────────────────────────────────
SECRET_KEY = config("SECRET_KEY")
ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="localhost").split(",")

# ─── Aplicações instaladas ────────────────────────────────────────────────────
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

LOCAL_APPS = [
    "apps.portfolio",  # nossa app principal
]

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS

# ─── Middleware ───────────────────────────────────────────────────────────────
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",   # serve arquivos estáticos em produção
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ─── URLs e WSGI ─────────────────────────────────────────────────────────────
ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"

# ─── Templates ───────────────────────────────────────────────────────────────
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # Django também busca templates dentro de cada app (APP_DIRS)
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                # contexto global do portfólio (nome, contatos, etc.)
                "apps.portfolio.context_processors.portfolio_info",
            ],
        },
    },
]

# ─── Banco de dados (padrão SQLite para desenvolvimento) ─────────────────────
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# ─── Validação de senhas ──────────────────────────────────────────────────────
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ─── Internacionalização ──────────────────────────────────────────────────────
LANGUAGE_CODE = "pt-br"
TIME_ZONE = "America/Sao_Paulo"
USE_I18N = True
USE_TZ = True

# ─── Arquivos estáticos ───────────────────────────────────────────────────────
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"   # pasta gerada pelo collectstatic
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# ─── Arquivos de mídia (uploads) ──────────────────────────────────────────────
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# ─── PK padrão ───────────────────────────────────────────────────────────────
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
