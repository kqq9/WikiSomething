from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('', views.login_view),
	path('signup/', views.signup),
	path('entry/', views.entry),
	path('wiki/', views.wiki)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
