from django import forms
from .models import User, University, Scholarship, program, Country


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']


class UniversityForm(forms.ModelForm):
    class Meta:
        model = University
        fields = ['name', 'scholarship_availability', 'description', 'university_type', 'cost', 'how_to_apply', 'on_campus_housing', 'campusview', 'geolocation', 'application_deadline', 'logo', 'pre_univ', 'author', 'programs_offered', 'location']


class ScholarshipForm(forms.ModelForm):
    class Meta:
        model = Scholarship
        fields = ['name', 'type', 'study_level', 'description', 'application_deadline', 'logo', 'author', 'programs_applicable', 'eligible_nationalities', 'university_applicable']


class programForm(forms.ModelForm):
    class Meta:
        model = program
        fields = ['name', 'description']


class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['name', 'continent']


