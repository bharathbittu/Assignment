from rest_framework import serializers
from django.utils.timezone import now
from .models import requesterData, riderData


class RequesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = requesterData
        fields = '__all__'

    # @property
    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['status'] = 'PENDING' if instance.Date_n_Time > now() else 'EXPIRED'
    #     return representation


class RiderSerializer(serializers.ModelSerializer):
    class Meta:
        model = riderData
        fields = '__all__'
