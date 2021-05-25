import uuid
from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import UUIDRequest
from api.serializers import UUIDSerializer


class UUIDAPIVIEW(APIView):
    """
    List all uuid, and create a new uuid.
    """

    def get(self, request):
        UUIDRequest.objects.create(uuid=str(uuid.uuid4()))
        uuid_dict = {}
        uuid_list = UUIDRequest.objects.all().order_by('-created').values('created', 'uuid')
        for uuid_value in uuid_list:
            uuid_dict[str(uuid_value.get('created'))] = uuid_value.get('uuid')
        return Response(uuid_dict)
