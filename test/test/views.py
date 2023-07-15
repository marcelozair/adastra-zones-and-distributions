import json

from django.shortcuts import render

from zones.api.serializers import ZoneSerializer
from zones.models import Zone


def home(request):
    zones_data = ZoneSerializer(Zone.objects.all(), many=True).data

    json_context = {
        'zones': zones_data
    }

    context = {
        'context_json': json.dumps(json_context)
    }

    return render(request, 'home.html', context)
