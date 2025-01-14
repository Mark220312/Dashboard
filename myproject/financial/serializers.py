from rest_framework import serializers
from .models import FinancialMovement

class FinancialMovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialMovement
        fields = '__all__'