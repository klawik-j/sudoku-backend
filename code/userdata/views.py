from rest_framework import viewsets

from .models import Account
from .serializers import AccountSerializer


# TO DO
# delete GET and LIST method - security issue
class AccountViewSet(viewsets.ModelViewSet):
    """ViewSet for Account Model."""

    serializer_class = AccountSerializer
    queryset = Account.objects.all()
    lookup_field = "username"
    # permission_classes = [IsAuthenticated]
