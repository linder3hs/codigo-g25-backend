from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
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
        try:
            if self.action in ['create', 'register']:
                permission_classes = [permissions.AllowAny]
            elif self.action in ['list']:
                permission_classes = [permissions.IsAdminUser]
            elif self.action in ['retrieve', 'update', 'partial_update', 'destroy']:
                permission_classes = [permissions.IsAuthenticated]
            else:
                permission_classes = [permissions.IsAuthenticated]

            return [permission() for permission in permission_classes]
        except Exception as e:
            print("ERROR IN get_permissions")
            print(e)
        


    def get_serializer_class(self):
        """
        En base a la action que hagamos debemos usar
        un serializer
        """
        try:
            if self.action in ['create', 'register']:
                return UserRegistrationSerializer
            elif self.action in ['update_profile']:
                return UserProfileUpdateSerializer
            return UserSerializer
        except Exception as e:
            print("ERROR IN get_serializer_class")
            print(e)

    def get_queryset(self):
        try:
            if self.request.user.is_staff:
                return User.objects.all()
            return User.objects.filter(id=self.request.user.id)
        except Exception as e:
            print("ERROR IN get_queryset")
            print(e)

    @action(detail=False, methods=['post'], permission_classes=[permissions.AllowAny])
    def register(self, request):
        try:
            serializer = UserRegistrationSerializer(data=request.data)

            if serializer.is_valid():
                user = serializer.save()
                refresh = RefreshToken.for_user(user)

                return Response({
                    'message': 'Usuario creado correctamente',
                    'user': UserSerializer(user).data,
                    'token': {
                        'refresh': str(refresh),
                        'access': str(refresh.access_token)
                    }
                }, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print("ERROR IN get_permissions")
            print(e)
