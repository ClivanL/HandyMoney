from .models import Receipts, Items,Person, ItemToPerson
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import PersonSerializer, ReceiptSerializer, ItemSerializer, ItemToPersonSerializer, GroupSerializer
from rest_framework.response import Response

# Create your views here.
class PersonViewSet(viewsets.ModelViewSet):
    queryset=Person.objects.all()
    serializer_class=PersonSerializer
    permission_classes=[permissions.AllowAny]

class ReceiptViewSet(viewsets.ModelViewSet):
    queryset=Receipts.objects.all()
    serializer_class=ReceiptSerializer
    permission_classes=[permissions.AllowAny]

class ItemViewSet(viewsets.ModelViewSet):
    queryset=Items.objects.all()
    serializer_class=ItemSerializer
    permission_classes=[permissions.AllowAny]

class ItemToPersonViewSet(viewsets.ModelViewSet):
    queryset=ItemToPerson.objects.all()
    serializer_class=ItemToPersonSerializer
    permission_classes=[permissions.AllowAny]

class GroupViewSet(viewsets.ModelViewSet):
    queryset=Person.objects.all()
    serializer_class=GroupSerializer