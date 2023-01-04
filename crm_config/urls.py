from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('crm_main.urls')),
    path('account/', include('account.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('crm_core/', include('crm_core.urls')),
    path('client/', include('client.urls')),
    path('team/', include('team.urls'))

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

