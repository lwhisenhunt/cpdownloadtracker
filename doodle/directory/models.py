from django.db import models

# Create your models here.

class Human(models.Model):
    name = models.CharField(max_length=25)
    is_buyer = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)
    email = models.EmailField(max_length=30)
    zip_code = models.PositiveIntegerField(default=00000)
    def __str__(self):
        return self.name

class Doodle(models.Model):
    name = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    weight = models.FloatField(blank=True, null=True)
    birthdate = models.DateTimeField(null=True)
    picture = models.CharField(default="", max_length=20)
    is_for_sale = models.BooleanField(default=False)
    owner = models.ForeignKey("Human", on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.name

class DoodleListing(models.Model):
    subject = models.CharField(max_length=25)
    doodle = models.ForeignKey("Doodle", on_delete=models.CASCADE, null=True)
    is_public = models.BooleanField(default=False)
    date_created = models.DateTimeField(null=True, auto_now_add=True)
    description = models.TextField(blank=True, null=True)
    cost = models.FloatField(default=2000)
    def __str__(self):
        return self.subject + "-" + self.doodle.name
