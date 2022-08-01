from .models import Receipt, Item,Person,Party
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import PersonSerializer, ReceiptSerializer, ItemSerializer, PartySerializer
from rest_framework.response import Response

# Create your views here.
class PersonViewSet(viewsets.ModelViewSet):
    queryset=Person.objects.all()
    serializer_class=PersonSerializer
    permission_classes=[permissions.AllowAny]

class ReceiptViewSet(viewsets.ModelViewSet):
    queryset=Receipt.objects.all()
    serializer_class=ReceiptSerializer
    permission_classes=[permissions.AllowAny]

class ItemViewSet(viewsets.ModelViewSet):
    queryset=Item.objects.all()
    serializer_class=ItemSerializer
    permission_classes=[permissions.AllowAny]

class PartyViewSet(viewsets.ModelViewSet):
    queryset=Party.objects.all()
    serializer_class=PartySerializer
    permission_classes=[permissions.AllowAny]