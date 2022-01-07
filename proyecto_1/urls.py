from django.urls import re_path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^login/', TemplateView.as_view(template_name = 'login/login.html'),
      name = 'login'),
    
]
