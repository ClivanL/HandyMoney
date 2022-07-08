from .models import Person, Receipts, Items, ItemToPerson
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Items
        fields=['id','itemName', 'price','receipt']

class ReceiptSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Receipts
        fields=['id', 'payer','person','details']

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Person
        fields=['id','personName','groupName']

class ItemToPersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=ItemToPerson
        fields=['id','item', 'person']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Person
        fields=['id','groupName']