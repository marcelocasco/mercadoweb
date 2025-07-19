from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.producto.urls')),  # Aquí conectamos las URLs de la app 'producto'
]

# Esta línea sirve para que en modo desarrollo se puedan cargar los archivos media (imágenes, etc.)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
