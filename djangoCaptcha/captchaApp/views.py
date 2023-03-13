from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import HumanOnlyDataSerializer

@api_view(['POST'])
def securityChecker(request):
   data = request.data
   serializer = HumanOnlyDataSerializer(data=data)
   if serializer.is_valid():
      return Response("verified")
   else:
      return Response("not verfied")