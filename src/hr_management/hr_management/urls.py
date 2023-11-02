from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("user.urls")),
    path('login/', include("django.contrib.auth.urls")),
    path('login/', include("authentication.urls")),
]
