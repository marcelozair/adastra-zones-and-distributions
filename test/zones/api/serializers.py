from rest_framework import serializers

from zones.models import Zone, Distribution


class DistributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distribution
        fields = ['id', 'percentage']


class ZoneSerializer(serializers.ModelSerializer):
    distributions = DistributionSerializer(many=True)

    class Meta:
        model = Zone
        fields = ['id', 'name', 'distributions']
