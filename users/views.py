from django.contrib.auth import get_user_model
from django.http import HttpRequest
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .permissions import CanAccessUserAPI
from .serializers import UserSerializer, UserActivitySerializer

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    permission_classes = [CanAccessUserAPI]

    @action(detail=True, methods=["get"])
    def activity(self, request: HttpRequest, pk: int = None) -> Response:
        return Response(UserActivitySerializer(self.get_object()).data)


