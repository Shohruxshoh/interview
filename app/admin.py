from django.contrib import admin
from .models import Customer, ExistingParty, Uzbek, Chinese

# Register your models here.

admin.site.register(Customer)
admin.site.register(ExistingParty)
admin.site.register(Uzbek)
admin.site.register(Chinese)
