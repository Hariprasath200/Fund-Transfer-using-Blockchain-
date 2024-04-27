# accounts/models.py
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Add custom fields if needed
    pass


# models.py
from django.db import models

import hashlib
from django.db import models

class Fund(models.Model):
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    mobile = models.CharField(max_length=15)
    email = models.EmailField()
    description = models.TextField()
    hash_value = models.CharField(max_length=64, editable=False)  # 64 characters for SHA-256 hash

    def save(self, *args, **kwargs):
        # Concatenate the fields and encode the data
        data = f"{self.name}{self.amount}{self.mobile}{self.email}{self.description}".encode()
        
        # Calculate the SHA-256 hash
        hash_object = hashlib.sha256(data)
        hex_dig = hash_object.hexdigest()
        
        # Store the hash value in the model
        self.hash_value = hex_dig
        
        super().save(*args, **kwargs)
# models.py
from django.db import models

class Transaction(models.Model):
    sender = models.CharField(max_length=100)
    recipient = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction from {self.sender} to {self.recipient}"

