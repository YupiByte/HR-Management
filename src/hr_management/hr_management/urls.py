"""
URL configuration for hr_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from req_leave.views import submit_leave_request, manage_leave_request


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("publication.urls")),
    path('ckeditor/',include('ckeditor_uploader.urls')),
    path('request/', include("req_leave.urls"))
    # path('request/', submit_leave_request, name='submit_leave_request'),
    # path('manage/', manage_leave_request, name='manage_leave_request')
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)