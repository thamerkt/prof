from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import AllowAny

from .models import Profil, ProfilMoral, PhysicalProfil, Service
from .serializers import (
    ProfileSerializer,
    ProfilMoralSerializer,
    PhysicalProfilSerializer,
    ServiceSerializer
)

# 🔹 Regular Profile ViewSet
class ProfilViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        user_id = self.request.query_params.get('user')
        queryset = Profil.objects.all()
        if user_id:
            queryset = queryset.filter(user_id=user_id)
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        return Response(self.get_serializer(instance).data, status=status.HTTP_201_CREATED)


# 🔹 Moral Profile ViewSet
class ProfilMoralViewSet(viewsets.ModelViewSet):
    serializer_class = ProfilMoralSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        profil_id = self.request.query_params.get('profil')
        queryset = ProfilMoral.objects.all()
        if profil_id:
            queryset = queryset.filter(profil_id=profil_id)
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        return Response(self.get_serializer(instance).data, status=status.HTTP_201_CREATED)


# 🔹 Physical Profile ViewSet (with file upload support)
class ProfilPhysiqueViewSet(viewsets.ModelViewSet):
    serializer_class = PhysicalProfilSerializer
    permission_classes = [AllowAny]
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        profil_id = self.request.query_params.get('profil')
        queryset = PhysicalProfil.objects.all()
        if profil_id:
            queryset = queryset.filter(profil_id=profil_id)
        return queryset

    def create(self, request, *args, **kwargs):
        # print("Received data:", request.data)  # Uncomment for debugging
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        return Response(self.get_serializer(instance).data, status=status.HTTP_201_CREATED)


# 🔹 Service ViewSet
class ServiceViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        partner_id = self.request.query_params.get('partner')
        queryset = Service.objects.all()
        if partner_id:
            queryset = queryset.filter(partenaire=partner_id)
        return queryset
