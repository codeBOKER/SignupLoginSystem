from django.contrib.auth.models import User
from account.serializers import PublicUserSerializer, PrivateUserSerializer
from account.permissions import IsOwnerOrAdmin
from rest_framework import mixins
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

class UsersList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    def get_serializer_class(self):
        if self.request.user.is_staff:
            return PrivateUserSerializer
        return PublicUserSerializer

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return self.list(request, *args, **kwargs)
        return Response({'error': 'Authentication required'}, status=status.HTTP_401_UNAUTHORIZED)

    def post(self, request, *args, **kwargs):
        serializer = PrivateUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'user': PrivateUserSerializer(user).data,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        user = self.get_object()
        if self.request.user == user or self.request.user.is_staff:
            return PrivateUserSerializer
        return PublicUserSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        user = self.get_object()
        if request.user == user or request.user.is_staff:
            return self.update(request, *args, **kwargs)
        return Response({'error': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        if request.user == user or request.user.is_staff:
            return self.destroy(request, *args, **kwargs)
        return Response({'error': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)
