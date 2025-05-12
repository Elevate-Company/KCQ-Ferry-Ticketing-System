from django.contrib import admin
from .models import FerryBoat, Trip, Passenger, Ticket, Log, Baggage
from django.utils.html import format_html
from django.contrib import messages

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
    list_display = ('name', 'email', 'phone', 'created_at', 'updated_at', 'deletion_requests_count')
    search_fields = ('name', 'email', 'phone')
    actions = ['delete_passenger_permanently']
    
    def deletion_requests_count(self, obj):
        """Count deletion requests for this passenger in the logs"""
        count = Log.objects.filter(
            model_name='Passenger',
            action='DELETE',
            object_id=str(obj.id)
        ).count()
        
        if count > 0:
            return format_html('<span style="color: red;">{}</span>', count)
        return count
    
    deletion_requests_count.short_description = 'Deletion Requests'
    
    def delete_passenger_permanently(self, request, queryset):
        """Admin action to permanently delete passengers after review"""
        for passenger in queryset:
            # Check if there are deletion requests in logs
            has_deletion_requests = Log.objects.filter(
                model_name='Passenger',
                action='DELETE',
                object_id=str(passenger.id)
            ).exists()
            
            if has_deletion_requests:
                # Create a log for admin permanent deletion
                Log.objects.create(
                    user=request.user,
                    action='DELETE',
                    model_name='Passenger',
                    object_id=str(passenger.id),
                    details=f"Admin permanently deleted passenger: {passenger.name}",
                    ip_address=self.get_client_ip(request)
                )
                
                # Perform actual deletion
                passenger.delete()
                messages.success(request, f"Permanently deleted passenger: {passenger.name}")
            else:
                messages.warning(request, f"No deletion requests found for passenger: {passenger.name}. Review skipped.")
    
    delete_passenger_permanently.short_description = "Permanently delete selected passengers after review"
    
    def get_client_ip(self, request):
        """Get client IP address from request"""
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

# Register Baggage model
@admin.register(Baggage)
class BaggageAdmin(admin.ModelAdmin):
    list_display = ('id', 'weight', 'free_weight_limit', 'excess_weight', 'excess_fee_per_kg', 'total_fee', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('id',)
    readonly_fields = ('excess_weight', 'total_fee')

# Register Ticket model
@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = (
        'ticket_number', 'passenger', 'trip', 'seat_number', 'age_group', 
        'price', 'issue_date', 'created_by', 'baggage_ticket', 'get_baggage_info'
        # Removing qr_code_image from display
    )
    search_fields = ('ticket_number', 'passenger__name', 'trip__origin', 'trip__destination')
    list_filter = ('age_group', 'issue_date', 'created_at', 'trip', 'baggage_ticket')
    readonly_fields = ['discount']  # Removed qr_code_image from readonly_fields
    
    def get_baggage_info(self, obj):
        if obj.baggage:
            return f"{obj.baggage.weight}kg (Fee: PHP{obj.baggage.total_fee})"
        return "-"
    get_baggage_info.short_description = 'Baggage Info'
    
    # Commenting out QR code image method
    # def qr_code_image(self, obj): 
    #     if obj.get_qr_code_url():
    #         return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.get_qr_code_url())
    #     return '-'
    # qr_code_image.short_description = 'QR Code'

# Register Log model
@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ('user', 'action', 'model_name', 'object_id', 'timestamp', 'ip_address')
    list_filter = ('action', 'model_name', 'user', 'timestamp')
    search_fields = ('user__username', 'action', 'model_name', 'object_id', 'details')
    readonly_fields = ('user', 'action', 'model_name', 'object_id', 'details', 'ip_address', 'timestamp')
    
    def has_add_permission(self, request):
        return False
        
    def has_change_permission(self, request, obj=None):
        return False