from rest_framework import serializers

from zones.models import Zone, Distribution


class DistributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distribution
        fields = ['id', 'percentage']

    def create(self, validated_data):
        return Distribution.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.percentage = validated_data.get('percentage', instance.percentage)
        instance.save()
        return instance


class ZoneSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    distributions = DistributionSerializer(many=True)

    class Meta:
        model = Zone
        fields = ['id', 'name', 'distributions', 'updated_at']

    def validate_name(self, value):
        length_name = len(value)

        if length_name == 0:
            raise serializers.ValidationError('The zone name cannot be empty')

        if "  " in value:
            raise serializers.ValidationError('The zone name cannot have more than one space between each word')

        return value
    