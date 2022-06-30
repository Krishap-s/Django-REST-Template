from django.contrib.auth import models
from rest_framework import serializers


class CurrentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('username','email','first_name','last_name','date_joined','last_login')