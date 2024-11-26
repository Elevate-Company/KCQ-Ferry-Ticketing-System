from django.db import models
from decimal import Decimal
from django.core.files.base import ContentFile
from io import BytesIO
from decimal import Decimal
from autoslug import AutoSlugField

from authentication.models import Account

import qrcode


class FerryBoat(models.Model):
    name = models.CharField(max_length=100, unique=True)
    capacity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = AutoSlugField(populate_from='name')

    def __str__(self):
        return self.name

class Trip(models.Model):
    ferry_boat = models.ForeignKey(FerryBoat, on_delete=models.CASCADE)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    available_seats = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.origin} to {self.destination} ({self.departure_time} - {self.arrival_time})"

class Passenger(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Ticket(models.Model):
    AGE_GROUP_CHOICES = [
        ('adult', 'Adult'),
        ('child', 'Child'),
        ('student', 'Student'),
        ('senior', 'Senior'),
        ('infant', 'Infant'),
    ]

    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    ticket_number = models.CharField(max_length=50, unique=True)
    seat_number = models.CharField(max_length=10, blank=True, null=True)
    age_group = models.CharField(max_length=7, choices=AGE_GROUP_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=400.00)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    issue_date = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(Account, on_delete=models.CASCADE)
    baggage_ticket = models.BooleanField(default=False)
    qr_code = models.ImageField(upload_to='tickets/qr_codes/', blank=True, null=True)  # Store QR code image

    def __str__(self):
        return f"Ticket {self.ticket_number} for {self.passenger.name}"

    def calculate_discount(self):
        if self.age_group == 'student':
            self.discount = self.price * Decimal('0.20')
        elif self.age_group == 'senior':
            self.discount = self.price * Decimal('0.20')
        elif self.age_group == 'child':
            self.discount = self.price * Decimal('0.50')
        elif self.age_group == 'infant':
            self.discount = self.price * Decimal('0.100')
        else:
            self.discount = Decimal('0.00')

    def generate_qr_code(self):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(self.ticket_number)
        qr.make(fit=True)

        img = qr.make_image(fill='black', back_color='white')

        buffer = BytesIO()
        img.save(buffer, format='PNG')
        buffer.seek(0)

        self.qr_code.save(f"{self.ticket_number}_qr.png", ContentFile(buffer.read()), save=False)

    def save(self, *args, **kwargs):
        self.calculate_discount()
        if not self.qr_code:
            self.generate_qr_code()
        super().save(*args, **kwargs)

    class Meta:
        unique_together = ('trip', 'seat_number')