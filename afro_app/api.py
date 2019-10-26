from . import models
from . import serializers
from rest_framework import viewsets, permissions


class UserViewSet(viewsets.ModelViewSet):
    """ViewSet for the User class"""

    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class UniversityViewSet(viewsets.ModelViewSet):
    """ViewSet for the University class"""

    queryset = models.University.objects.all()
    serializer_class = serializers.UniversitySerializer
    permission_classes = [permissions.IsAuthenticated]


class ScholarshipViewSet(viewsets.ModelViewSet):
    """ViewSet for the Scholarship class"""

    queryset = models.Scholarship.objects.all()
    serializer_class = serializers.ScholarshipSerializer
    permission_classes = [permissions.IsAuthenticated]


class programViewSet(viewsets.ModelViewSet):
    """ViewSet for the program class"""

    queryset = models.program.objects.all()
    serializer_class = serializers.programSerializer
    permission_classes = [permissions.IsAuthenticated]


class CountryViewSet(viewsets.ModelViewSet):
    """ViewSet for the Country class"""

    queryset = models.Country.objects.all()
    serializer_class = serializers.CountrySerializer
    permission_classes = [permissions.IsAuthenticated]


