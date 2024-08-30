from django.db import models

class GeoLocation(models.Model):
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lng = models.DecimalField(max_digits=9, decimal_places=6)

class Address(models.Model):
    street = models.CharField(max_length=255)
    suite = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=20)
    geolocation = models.OneToOneField(GeoLocation, on_delete=models.CASCADE)

class Company(models.Model):
    name = models.CharField(max_length=255)

class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    website = models.URLField(max_length=200)
    company = models.OneToOneField(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
