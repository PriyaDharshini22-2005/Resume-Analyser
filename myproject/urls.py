from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import TemplateView
from api.views import upload_file

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/upload/', upload_file, name='upload_file'),
    re_path(r'^.*$', TemplateView.as_view(template_name='index.html'), name='index'),
]
