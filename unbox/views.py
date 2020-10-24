from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def apiOverview(request):
    data = {"error": "not a valid endpoint"}
    return Response(data)
