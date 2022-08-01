from django.db import models

# Create your models here.

class Party(models.Model):
    partyName=models.CharField(max_length=100, default="default")

class Person(models.Model):
    personName=models.CharField(max_length=100)
    party=models.ForeignKey(Party, related_name="person", on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % (self.personName)

class Receipt(models.Model):
    payer=models.ForeignKey(Person, on_delete=models.CASCADE)
    details=models.CharField(max_length=100, default="not entered")
    party=models.ForeignKey(Party, related_name="receipt", on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.details, self.payer)

class Item(models.Model):
    itemName=models.CharField(max_length=100)
    price=models.FloatField()
    receipt=models.ForeignKey(Receipt, related_name="item",on_delete=models.CASCADE)

    def __str__(self):
        return '%s %f' % (self.itemName, self.price)







# class ItemToPerson(models.Model):
#     item=models.ForeignKey(Item,on_delete=models.CASCADE)
#     person=models.ForeignKey(Person, on_delete=models.CASCADE)
    
    