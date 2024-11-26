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
    list_display = ('name', 'contact', 'created_at', 'updated_at')
    search_fields = ('name', 'contact')

# Register Ticket model
@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = (
        'ticket_number', 'passenger', 'trip', 'seat_number', 'age_group', 'price', 'issue_date', 'created_by', 'baggage_ticket', 'qr_code_image'
    )
    search_fields = ('ticket_number', 'passenger__name', 'trip__origin', 'trip__destination')
    list_filter = ('age_group', 'issue_date', 'created_at', 'trip')
    readonly_fields = ['discount']
    
    # Display QR Code in admin panel
    def qr_code_image(self, obj):
        return format_html('<img src="{}" style="width: 100px; height: auto;" />'.format(obj.qr_code.url) if obj.qr_code else '')
    qr_code_image.short_description = 'QR Code'