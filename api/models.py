from django.db import models
from decimal import Decimal
from django.core.files.base import ContentFile
from io import BytesIO
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
    BOARDING_STATUS_CHOICES = [
        ('NOT_BOARDED', 'Not Boarded'),
        ('BOARDED', 'Boarded'),
        ('CANCELLED', 'Cancelled'),
    ]

    name = models.CharField(max_length=100)
    email = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    total_bookings = models.PositiveIntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)
    boarding_status = models.CharField(
        max_length=15,  # Length of the longest choice key
        choices=BOARDING_STATUS_CHOICES,
        default='NOT_BOARDED'
    )

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
    
    PAYMENT_METHOD_CHOICES = [
        ('CASH', 'Cash'),
        ('GCASH', 'GCash'),
        ('MAYA', 'Maya'),
    ]

    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    ticket_number = models.CharField(max_length=50, unique=True)
    seat_number = models.CharField(max_length=10, blank=True, null=True)
    age_group = models.CharField(max_length=7, choices=AGE_GROUP_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=400.00)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    payment_method = models.CharField(max_length=5, choices=PAYMENT_METHOD_CHOICES, default='CASH')
    payment_reference = models.CharField(max_length=50, blank=True, null=True, help_text="Reference number for online payments")
    cash_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    issue_date = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(Account, on_delete=models.CASCADE)
    baggage_ticket = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)
    # Commenting out QR code field for now
    # qr_code = models.ImageField(upload_to='tickets/qr_codes/', blank=True, null=True)

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

    # Commenting out QR code generation methods
    # def generate_qr_code(self):
    #     if not self.ticket_number:
    #         return
            
    #     qr = qrcode.QRCode(
    #         version=1,
    #         error_correction=qrcode.constants.ERROR_CORRECT_L,
    #         box_size=10,
    #         border=4,
    #     )
    #     qr.add_data(self.ticket_number)
    #     qr.make(fit=True)

    #     img = qr.make_image(fill='black', back_color='white')
    #     buffer = BytesIO()
    #     img.save(buffer, format='PNG')
    #     buffer.seek(0)

    #     self.qr_code.save(f"{self.ticket_number}_qr.png", ContentFile(buffer.read()), save=False)

    # def get_qr_code_url(self):
    #     if self.qr_code:
    #         return self.qr_code.url
    #     return None

    def save(self, *args, **kwargs):
        self.calculate_discount()
        super().save(*args, **kwargs)  # Save without QR code generation

    class Meta:
        unique_together = ('trip', 'seat_number')

class Log(models.Model):
    ACTION_CHOICES = [
        ('CREATE', 'Create'),
        ('UPDATE', 'Update'),
        ('DELETE', 'Delete'),
        ('LOGIN', 'Login'),
        ('LOGOUT', 'Logout'),
        ('OTHER', 'Other'),
    ]

    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='logs')
    action = models.CharField(max_length=10, choices=ACTION_CHOICES)
    model_name = models.CharField(max_length=50)  # The model that was affected
    object_id = models.CharField(max_length=50, null=True, blank=True)  # ID of the affected object
    details = models.TextField(null=True, blank=True)  # Additional details
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']
        verbose_name = 'Activity Log'
        verbose_name_plural = 'Activity Logs'

    def __str__(self):
        return f"{self.user} - {self.action} {self.model_name} at {self.timestamp}"