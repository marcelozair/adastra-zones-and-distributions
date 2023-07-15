from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from zones.models import Zone


@api_view(['POST'])
def edit(request):
    zone_id = request.data.get('id')
    name = request.data.get('name')

    zone = Zone.objects.filter(pk=zone_id).first()
    if not zone:
        return Response('', status=status.HTTP_400_BAD_REQUEST)

    zone.name = name
    zone.save()

    return Response()
