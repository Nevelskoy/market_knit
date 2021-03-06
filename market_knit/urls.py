from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls import include

import mainapp.views as mainapp

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', mainapp.main, name='main'),
    path('list_of_accommodations/', include('mainapp.urls', namespace='acc')),
    path('auth/', include('authapp.urls', namespace='auth')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
