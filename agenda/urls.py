from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from contatos.api.viewsets import ContatoViewSet

router = routers.DefaultRouter()
router.register('contatos', ContatoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
