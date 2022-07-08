from .models import Person, Receipt, Item
from django.contrib.auth.models import User, Group
from rest_framework import serializers

# class PartySerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model=Party
#         fields=['id','partyName']


class ReceiptSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Receipt
        fields=['id', 'payer','party','details']

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Person
        fields=['id','personName','party']


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    # itemName = serializers.HyperlinkedIdentityField(
    #     view_name='item-detail'
    # )
    # receipt = serializers.HyperlinkedRelatedField(
    #     view_name='receipt-detail',
    #     # many=True,
    #     read_only=True
    # )
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
