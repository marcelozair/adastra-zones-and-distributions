from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.db.models import Q
from zones.models import Zone, Distribution
from zones.api.serializers import ZoneSerializer, DistributionSerializer

@api_view(['PUT'])
def edit(request):
    zone_serializer = ZoneSerializer(data=request.data)
    zone_serializer.is_valid(raise_exception=True)

    zona_name = zone_serializer.data['name']
    zone_id = zone_serializer.data['id']

    distributions = request.data.get('distributions')
    deletedDistributions = request.data.get('deletedDistributions')

    zone = Zone.objects.get(pk=zone_id)

    if not zone:
        return Response('', status=status.HTTP_400_BAD_REQUEST)

    zone_exists_repeat = Zone.objects.filter(name=zona_name).exclude(id=zone_id).first()

    if zone_exists_repeat:
        return Response(
            { 'message': 'Already exist a zone with the same name' },
            status=status.HTTP_400_BAD_REQUEST
        )

    total_distribution = 0

    for distribution in distributions:
        total_distribution = total_distribution + distribution['percentage']
    
    if total_distribution != 100:
        return Response(
            { 'message': 'The sum of all distributions must be ensured to be 100%' },
            status=status.HTTP_400_BAD_REQUEST
        )

    
    for distribution in deletedDistributions:
        # Remove distributions
        distributionFound = Distribution.objects.filter(pk=distribution['id']).first()
        if distributionFound:
            distributionFound.delete()

    for distribution in distributions:
        if distribution['isNew']:
            # Create new distributions
            Distribution.objects.create(zone=zone, percentage=distribution['percentage'])
        else:
            # Update distributions
            distributionFound = Distribution.objects.filter(pk=distribution['id']).first()
            if not distributionFound:
                return Response('', status=status.HTTP_400_BAD_REQUEST)
        
            distributionFound.percentage = distribution['percentage']
            distributionFound.save()

    zone.name = zona_name
    zone.save()

    return Response('', status=status.HTTP_202_ACCEPTED)
