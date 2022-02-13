from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapi.urls')),
   # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   # path('login', views.login_view),
    url(r'^$', TemplateView.as_view(template_name='static_pages/index.html'), name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
