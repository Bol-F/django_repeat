from .serializers import AccountSerializer, AccountRegisterSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny


class RegisterAPIView(generics.CreateAPIView):
    serializer_class = AccountRegisterSerializer
    permission_classes = [AllowAny]


class MeAPIView(generics.RetrieveAPIView):
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
