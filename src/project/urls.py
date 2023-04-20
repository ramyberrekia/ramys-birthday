from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('secret/', admin.site.urls),
    path('', include('message.urls', namespace='message')),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
handler404 = "project.views.page_not_found_view"
