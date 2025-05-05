from rest_framework import serializers
from api.models import Log

class LogSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    
    class Meta:
        model = Log
        fields = ['id', 'user', 'action', 'model_name', 'object_id', 'details', 'ip_address', 'timestamp']
        read_only_fields = fields 