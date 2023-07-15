from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from zones.models import Zone, Distribution


@api_view(['PUT'])
def edit(request):
    zone_id = request.data.get('id')
    name = request.data.get('name')
    distributions = request.data.get('distributions')
    deletedDistributions = request.data.get('deletedDistributions')

    zone = Zone.objects.filter(pk=zone_id).first()

    if not zone:
        return Response('', status=status.HTTP_400_BAD_REQUEST)
    
    for distribution in deletedDistributions:
        # Remove distributions
        distributionFound = Distribution.objects.filter(pk=distribution["id"]).first()
        if distributionFound:
            distributionFound.delete()

    for distribution in distributions:
        if distribution["isNew"]:
            # Create new distributions
            Distribution.objects.create(zone=zone, percentage=distribution["percentage"])
        else:
            # Update distributions
            distributionFound = Distribution.objects.filter(pk=distribution["id"]).first()
            if not distributionFound:
                return Response('', status=status.HTTP_400_BAD_REQUEST)
        
            distributionFound.percentage = distribution["percentage"]
            distributionFound.save()

    zone.name = name
    zone.save()

    return Response('', status=status.HTTP_202_ACCEPTED)
