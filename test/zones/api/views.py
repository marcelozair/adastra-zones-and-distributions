from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from zones.models import Zone, Distribution


@api_view(['PUT'])
def edit(request):
    zone_id = request.data.get('id')
    name = request.data.get('name')
    distributionsEdited = request.data.get('distributions')

    zone = Zone.objects.filter(pk=zone_id).first()
    if not zone:
        return Response('', status=status.HTTP_400_BAD_REQUEST)

    for distribution in distributionsEdited:
        distributionFound = Distribution.objects.filter(pk=distribution["id"]).first()
        if not distributionFound:
            return Response('', status=status.HTTP_400_BAD_REQUEST)
        
        distributionFound.percentage = distribution["percentage"]
        distributionFound.save()

    zone.name = name
    zone.save()

    return Response('', status=status.HTTP_202_ACCEPTED)
