from django.contrib import admin
from expenses.models import Person, Item, Receipt

# Register your models here.
# admin.site.register(Party)
admin.site.register(Person)
admin.site.register(Item)
admin.site.register(Receipt)