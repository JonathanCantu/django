from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from elements import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name='index'),
    path("elements/", include("elements.urls")),
    path("demoApp/", include('demoApp.urls')),
]

