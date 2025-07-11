from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import UserActivity, EmailVerificationToken
from .serializers import (
  UserSerializer,
  UserRegistrationSerializer,
  UserProfileUpdateSerializer,
  LoginSerializer,
)



@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def verify_email(request):
    token = request.data.get('token')

    if not token:
        return Response({
            'error': 'Token no encontrado'
        }, status=status.HTTP_400_BAD_REQUEST)

    try:
        verification_token = EmailVerificationToken.objects.get(token=token)

        if not verification_token.is_valid():
            return Response({
            'error': 'Token Invalid or Expires'
        }, status=status.HTTP_400_BAD_REQUEST)

        user = verification_token.user
        user.is_active = True
        user.save()

        user.profile.email_verified = True
        user.profile.save()

        verification_token.mark_as_used()

        return Response({
            'message': 'Email verified successly.'
        })
    except Exception as e:
        return Response({
            'error': 'Token Invalid'
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def login_view(request):
    serializer = LoginSerializer(data=request.data)

    """ Si no es valido retornamos un 400 """
    if not serializer.is_valid() :
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    username = serializer.validated_data['username']
    password = serializer.validated_data['password']

    # Buscar si es un username o un email
    user = None

    if '@' in username:
        try:
            user = User.objects.get(email=username)
            username = user.username
        except User.DoesNotExist:
            pass
    else:
        user = User.objects.get(username=username)

    if not user.is_active:
        return Response({
            'error': 'Necesitas activar tu cuenta para iniciar sesión'
        }, status=status.HTTP_401_UNAUTHORIZED)

    authenticated_user = authenticate(username=username, password=password)

    if authenticated_user:
        UserActivity.objects.create(
            user=authenticated_user,
            action='LOGIN',
            ip_address=get_ip_address(request),
            user_agent=get_user_agent(request),
            details={'login_method': 'username_password'}
        )

        refresh = RefreshToken.for_user(authenticated_user)

        return Response({
            'message': 'Login exitoso',
            'user': UserSerializer(authenticated_user).data,
            'tokens': {
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }
        })
    else:
        if user:
            UserActivity.objects.create(
                user=user,
                action='FAILED_LOGIN',
                ip_address=get_ip_address(request),
                user_agent=get_user_agent(request),
                details={'login_failed': 'error in authentication'}
            )

        return Response({
            'message': 'Login faleid',
            'error': 'Hubo un error en la autenticación'
        }, status=status.HTTP_401_UNAUTHORIZED)


def get_ip_address(request):
    return request.META.get('REMOTE_ADDR')

def get_user_agent(request):
    return request.META.get('HTTP_USER_AGENT')


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
