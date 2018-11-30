from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import RiskType
from .serializers import RiskTypeSerializer, RiskSerializer


class RiskTypeList(APIView):
    """
    List all risk types, or create a new one.
    """

    def get(self, request, format=None):
        risk_types = RiskType.objects.all()
        serializer = RiskTypeSerializer(risk_types, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RiskTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RiskList(APIView):
    """
    List all risk, or create a new one.
    """

    def get(self, request, format=None):
        risk_types = Risk.objects.all()
        serializer = RiskSerializer(risk_types, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RiskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RiskTypeDetail(APIView):
    """
    Retrieve, update or delete a risk_type instance.
    """

    def get_object(self, pk):
        try:
            return RiskType.objects.get(pk=pk)
        except RiskType.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        risk_type = self.get_object(pk)
        serializer = RiskTypeSerializer(risk_type)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        risk_type = self.get_object(pk)
        serializer = RiskTypeSerializer(risk_type, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        risk_type = self.get_object(pk)
        risk_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
