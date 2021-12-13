
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('book/', include('bookstore.urls'))


] + static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT) \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
