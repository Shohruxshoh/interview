from django.db import models
import datetime


# Create your models here.

class Customer(models.Model):
    name_surname = models.CharField(max_length=200, null=True, blank=True)
    telegram_id = models.CharField(max_length=200, null=True, blank=True)
    key_word = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.key_word}"


class ExistingParty(models.Model):
    party_name = models.CharField(max_length=200, null=True, blank=True)
    register_date = models.DateField(default=datetime.datetime.utcnow)

    def __str__(self):
        return f"{self.party_name}"


class Chinese(models.Model):
    party = models.ForeignKey(ExistingParty, on_delete=models.SET_NULL, null=True, blank=True)
    track_code = models.CharField(max_length=200, null=True, blank=True)
    item_name = models.CharField(max_length=200, null=True, blank=True)
    customer_key = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    item_number = models.IntegerField(default=0)
    item_weight = models.FloatField(default=0.0)
    box_name = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.track_code}"


class Uzbek(models.Model):
    party = models.ForeignKey(ExistingParty, on_delete=models.SET_NULL, null=True, blank=True)
    track_code = models.ForeignKey(Chinese, on_delete=models.SET_NULL, null=True, blank=True)
    customer_key = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    price_per_kg = models.FloatField(default=0.0)
    item_weight = models.FloatField(default=0.0)
    paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.track_code}-{self.party}"
