from django.db import models

# Create your models here.

class Party(models.Model):
    partyName=models.CharField(max_length=100, default="default")

class Person(models.Model):
    personName=models.CharField(max_length=100)
    party=models.ForeignKey(Party,on_delete=models.CASCADE)

class Receipt(models.Model):
    payer=models.CharField(max_length=100,default="user")
    details=models.CharField(max_length=100, default="not entered")
    party=models.ForeignKey(Party, on_delete=models.CASCADE)

class Item(models.Model):
    itemName=models.CharField(max_length=100)
    price=models.FloatField()
    receipt=models.ForeignKey(Receipt, on_delete=models.CASCADE)







# class ItemToPerson(models.Model):
#     item=models.ForeignKey(Item,on_delete=models.CASCADE)
#     person=models.ForeignKey(Person, on_delete=models.CASCADE)
    
    