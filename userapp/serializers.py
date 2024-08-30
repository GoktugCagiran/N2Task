from rest_framework import serializers
from .models import User, Address, GeoLocation, Company

class GeoLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeoLocation
        fields = ['lat', 'lng']

class AddressSerializer(serializers.ModelSerializer):
    geolocation = GeoLocationSerializer()

    class Meta:
        model = Address
        fields = ['street', 'suite', 'city', 'zipcode', 'geolocation']

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name']

class UserSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    company = CompanySerializer()

    class Meta:
        model = User
        fields = ['id', 'name', 'username', 'email', 'address', 'phone', 'website', 'company']

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        geolocation_data = address_data.pop('geolocation')
        company_data = validated_data.pop('company')

        geolocation = GeoLocation.objects.create(**geolocation_data)
        address = Address.objects.create(geolocation=geolocation, **address_data)
        company = Company.objects.create(**company_data)
        user = User.objects.create(address=address, company=company, **validated_data)
        return user

    def update(self, instance, validated_data):
        address_data = validated_data.pop('address', None)
        geolocation_data = address_data.pop('geolocation', None) if address_data else None
        company_data = validated_data.pop('company', None)

        if address_data and geolocation_data:
            geolocation = instance.address.geolocation
            geolocation.lat = geolocation_data.get('lat', geolocation.lat)
            geolocation.lng = geolocation_data.get('lng', geolocation.lng)
            geolocation.save()

            address = instance.address
            address.street = address_data.get('street', address.street)
            address.suite = address_data.get('suite', address.suite)
            address.city = address_data.get('city', address.city)
            address.zipcode = address_data.get('zipcode', address.zipcode)
            address.save()

        if company_data:
            company = instance.company
            company.name = company_data.get('name', company.name)
            company.save()

        instance.name = validated_data.get('name', instance.name)
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.website = validated_data.get('website', instance.website)
        instance.save()

        return instance
