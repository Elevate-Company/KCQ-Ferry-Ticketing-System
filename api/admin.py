from django.contrib import admin
from .models import FerryBoat, Trip, Passenger, Ticket
from django.utils.html import format_html

# Register FerryBoat model
@admin.register(FerryBoat)
class FerryBoatAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity', 'slug', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('created_at', 'updated_at')

# Register Trip model
@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ('ferry_boat', 'origin', 'destination', 'departure_time', 'arrival_time', 'available_seats', 'created_at', 'updated_at')
    search_fields = ('origin', 'destination', 'ferry_boat__name')
    list_filter = ('departure_time', 'arrival_time', 'ferry_boat')

# Register Passenger model
@admin.register(Passenger)
class PassengerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at', 'updated_at')
    search_fields = ('name', 'email', 'phone')

# Register Ticket model
@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = (
        'ticket_number', 'passenger', 'trip', 'seat_number', 'age_group', 
        'price', 'issue_date', 'created_by', 'baggage_ticket'
        # Removing qr_code_image from display
    )
    search_fields = ('ticket_number', 'passenger__name', 'trip__origin', 'trip__destination')
    list_filter = ('age_group', 'issue_date', 'created_at', 'trip')
    readonly_fields = ['discount']  # Removed qr_code_image from readonly_fields
    
    # Commenting out QR code image method
    # def qr_code_image(self, obj):
    #     if obj.get_qr_code_url():
    #         return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.get_qr_code_url())
    #     return '-'
    # qr_code_image.short_description = 'QR Code'