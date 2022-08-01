from .models import Person, Receipt, Item,Party
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class PartySerializer(serializers.ModelSerializer):
    person=serializers.StringRelatedField(many=True)
    receipt=serializers.StringRelatedField(many=True)
    class Meta:
        model=Party
        fields=['id','partyName','person', 'receipt']


class ReceiptSerializer(serializers.HyperlinkedModelSerializer):
    item=serializers.StringRelatedField(many=True)
    class Meta:
        model=Receipt
        fields=['id', 'payer','details','party','item']

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Person
        fields=['id','personName','party']


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Item
        fields=['id','itemName', 'price','receipt']
        extra_kwargs={
            'receipt':{'view_name':'receipt-detail'}
        }




# class ItemToPersonSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model=ItemToPerson
#         fields=['id','item', 'person']
