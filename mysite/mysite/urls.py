from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('battleship/', include('battleship.urls')),
    path('admin/', admin.site.urls),
]
