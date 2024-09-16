from rest_framework import serializers
from .models import Blog

class BlogReadOnlySerializer(serializers.ModelSerializer):
    writer_name = serializers.ReadOnlyField(source='user.username')
    writer_email = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Blog
        fields = '__all__'
