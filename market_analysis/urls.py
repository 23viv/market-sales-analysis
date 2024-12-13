
from django.contrib import admin
from django.urls import path
from django.conf import settings  
from django.conf.urls.static import static 
from django.urls import include
from django.shortcuts import redirect
from analysis import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'), 
    path('upload/', include('analysis.urls')),  # Include URLs for the analysis app
    path('results/', include('analysis.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
