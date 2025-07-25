from rest_framework import serializers
from api.serializers import UserPublicSerializer
from .models import Countdown
from django.utils import timezone

class CountdownSerializer(serializers.ModelSerializer):
    user = UserPublicSerializer(read_only=True)
    remaining_time = serializers.SerializerMethodField(read_only=True)
    has_ended = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Countdown
        fields = [
            'id',
            'name',
            'target_time',
            'remaining_time',
            'has_ended',
            'user',
            'description',
            'isActive',
            'public',
        ]

    def get_remaining_time(self, obj):
        now = timezone.now()
        time_difference = obj.target_time - now
        print(time_difference.total_seconds())
        if time_difference.total_seconds() <= 0:
            return "0 days, 0 hours, 0 minutes, 0 seconds" # Countdown has ended or is in the past

        days = time_difference.days
        seconds = time_difference.seconds
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        remaining_seconds = seconds % 60

        return f"{days} days, {hours} hours, {minutes} minutes, {remaining_seconds} seconds"
    
    
    def get_has_ended(self,obj):
        now = timezone.now() # Get the current timezone-aware time
        return obj.target_time <= now
                                