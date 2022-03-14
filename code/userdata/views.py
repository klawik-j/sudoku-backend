from typing import List

from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser

from .models import Account
from .serializers import AccountSerializer


# TO DO
# delete GET and LIST method - security issue
class AccountViewSet(viewsets.ModelViewSet):
    """ViewSet for Account Model."""

    serializer_class = AccountSerializer
    queryset = Account.objects.all()
    lookup_field = "username"

    def get_permissions(self) -> List[str]:
        """Instantiate and return the list of permissions that this ViewSet requires."""
        if self.action == "list" or self.action == "create":
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
