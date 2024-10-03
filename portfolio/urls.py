from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('Dboy/', admin.site.urls),
    path('', include('resume.urls'))
]
