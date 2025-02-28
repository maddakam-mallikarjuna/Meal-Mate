from django.db import models

class Users(models.Model):
    USER_TYPES = [
        ('admin', 'Admin'),
        ('user', 'User'),
    ]

    username = models.CharField(max_length=150)
    email = models.EmailField(unique=True)  # Enforces uniqueness at the database level
    password = models.CharField(max_length=128)
    mobile = models.CharField(max_length=15)  # You can also validate mobile numbers
    address = models.TextField()
    usertype = models.CharField(max_length=10, choices=USER_TYPES)  # Choices added

    def __str__(self):
        return f"{self.username} ({self.usertype})"
