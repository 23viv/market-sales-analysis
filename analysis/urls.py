from django.urls import path
from . import views  # Import views from the current app

urlpatterns = [
    path('upload/', views.upload_file, name='upload_file'),  # URL for the upload page
    path('result/', views.result, name='result'),        # URL for the results page
]



