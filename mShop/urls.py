from django.conf.urls.static import static
from mShop import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("shop.urls")),
]
urlpatterns += static(settings.MEDIA_ROOT, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
