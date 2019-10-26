from . import models

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = (
            'pk', 
            'username', 
        )


class UniversitySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.University
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
            'scholarship_availability', 
            'description', 
            'university_type', 
            'cost', 
            'how_to_apply', 
            'on_campus_housing', 
            'campusview', 
            'geolocation', 
            'application_deadline', 
            'logo', 
            'pre_univ', 
        )


class ScholarshipSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Scholarship
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
            'type', 
            'study_level', 
            'description', 
            'application_deadline', 
            'logo', 
        )


class programSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.program
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
            'description', 
        )


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Country
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
            'continent', 
        )


