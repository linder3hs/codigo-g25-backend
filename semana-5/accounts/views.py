from rest_framework import viewsets, permissions
from django.contrib.auth.models import User
from .serializers import (
  UserSerializer,
  UserRegistrationSerializer,
  UserProfileUpdateSerializer
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action in ['create', 'register']:
            permission_classes = [permissions.AllowAny]
        elif self.action in ['list']:
            permission_classes = [permissions.IsAdminUser]
        elif self.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.IsAuthenticated]

        return [permission() for permission in permission_classes]


    def get_serializer_class(self):
        """
        En base a la action que hagamos debemos usar
        un serializer
        """
        if self.action in ['create', 'register']:
            return UserRegistrationSerializer
        elif self.action in ['update_profile']:
            return UserProfileUpdateSerializer
        return UserSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return User.objects.all()
        return User.objects.filter(id=self.request.user.id)
