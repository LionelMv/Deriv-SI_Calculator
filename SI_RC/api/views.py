from rest_framework import status, viewsets
from rest_framework.response import Response
from .serializers import RiskCalculationSerializer


class RiskCalculationViewSet(viewsets.ViewSet):
    serializer_class = RiskCalculationSerializer

    def create(self, request):
        serializer = RiskCalculationSerializer(data=request.data)

        if serializer.is_valid():
            result = serializer.to_representation(serializer)
            return Response(result)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
