from django.db import models

# Create your models here.

class Group(models.Model):
    groupName=models.CharField(max_length=100, default="default")

class Person(models.Model):
    personName=models.CharField(max_length=100)
    group=models.ForeignKey(Group,on_delete=models.CASCADE)

class Receipts(models.Model):
    payer=models.CharField(max_length=100,default="user")
    details=models.CharField(max_length=100, default="not entered")
    group=models.ForeignKey(Group, on_delete=models.CASCADE)

class Items(models.Model):
    itemName=models.CharField(max_length=100)
    price=models.IntegerField()
    receipt=models.ForeignKey(Receipts, on_delete=models.CASCADE)

class ItemToPerson(models.Model):
    item=models.ForeignKey(Items,on_delete=models.CASCADE)
    person=models.ForeignKey(Person, on_delete=models.CASCADE)
    
    