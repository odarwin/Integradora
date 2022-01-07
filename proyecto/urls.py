
from django.contrib import admin
from django.urls import include,re_path
from django.views.generic import RedirectView
from django.conf import settings
from django.views.generic import TemplateView
from django.conf.urls.static import static

urlpatterns = [
    re_path(r'admin/', admin.site.urls),
    re_path(r'proyecto_1/', include('proyecto_1.urls')),

    # re_path(r'', RedirectView.as_view(url='/proyecto_1/', permanent=True)),
]
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
