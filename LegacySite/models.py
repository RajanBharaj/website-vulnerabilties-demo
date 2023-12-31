from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.backends import BaseBackend
from . import extras
from fernet_fields import *

# Create your models here.
class User(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=97)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password']

class OurBackend(BaseBackend):
    def authenticate(self, request, username, password):
        assert(None not in [username, password])
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None
        pwrd_valid = extras.check_password(user, password)
        if pwrd_valid:
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50, unique=True)
    # Encrypted product image path [rtb325]
    product_image_path = EncryptedCharField(max_length=100)
    # Encrypted product recommended price [rtb325]
    recommended_price = EncryptedIntegerField()
    description = models.CharField(max_length=250)

class Card(models.Model):
    id = models.AutoField(primary_key=True)
    # Encrypted card data [rtb325]
    data = EncryptedCharField(max_length=1000)
    product = models.ForeignKey('LegacySite.Product', on_delete=models.CASCADE, default=None)
    # Encrypted card amount [rtb325]
    amount = EncryptedIntegerField()
    # Encrypted card file path [rtb325]
    fp = EncryptedCharField(max_length=100)
    user = models.ForeignKey('LegacySite.User', on_delete=models.CASCADE)
    used = models.BooleanField(default=False)
