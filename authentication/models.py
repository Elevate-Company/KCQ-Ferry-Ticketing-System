from django.db import models
from django.contrib.auth.models import AbstractUser
from enum import Enum

class Role(Enum):
    ADMIN = "admin"
    EMPLOYEE = "employee"

class Account(AbstractUser):
    # Custom fields
    role = models.CharField(
        max_length=20,
        choices=[(role.name, role.value) for role in Role],
        default=Role.EMPLOYEE.name,
    )
    mobile_number = models.CharField(max_length=15, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username