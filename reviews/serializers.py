from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    reviewer_name = serializers.ReadOnlyField(source='user.username')
    reviewer_email = serializers.ReadOnlyField(source='user.email')
    class Meta:
        model = Review
        fields = '__all__'


