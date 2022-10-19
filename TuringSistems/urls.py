
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from django.views.generic import TemplateView
from django.conf import settings
urlpatterns = [
    path("admin/", admin.site.urls),
    path('',TemplateView.as_view(template_name='index.html')),
    path('', include('Users.urls'))
]

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT})
]