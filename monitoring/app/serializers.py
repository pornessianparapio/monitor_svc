from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Admin

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ['admin_name', 'admin_email', 'admin_password']

    def validate_admin_password(self, value):
        """Hash the password before saving."""
        return make_password(value)