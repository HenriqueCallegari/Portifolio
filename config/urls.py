"""
URLs raiz do projeto.
Cada app registra suas próprias URLs — aqui apenas fazemos o include.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),

    # App portfolio ocupa a raiz do site
    path("", include("apps.portfolio.urls", namespace="portfolio")),
]

# Em desenvolvimento, o Django serve os arquivos de mídia (uploads)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
