from django.contrib import admin
from django.urls import include, path
from min_dup import views as min_dup_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('about/', min_dup_views.about, name='about'),
    path('', include('min_dup.urls')),
]