from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ( ProfilViewSet, ProfilMoralViewSet,ProfilPhysiqueViewSet,ServiceViewSet)
router = DefaultRouter()
router.register(r'profil', ProfilViewSet, basename='profil')
router.register(r'profilmoral', ProfilMoralViewSet, basename='profilmoral')  
router.register(r'physicalprofil', ProfilPhysiqueViewSet, basename='profilphysique')
router.register(r'services', ServiceViewSet, basename='services')
urlpatterns = [
    
]

urlpatterns += router.urls