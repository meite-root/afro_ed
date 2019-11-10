from django.contrib import admin
from django import forms
from .models import University, Scholarship, program, Country


class UniversityAdminForm(forms.ModelForm):

    class Meta:
        model = University
        fields = '__all__'


class UniversityAdmin(admin.ModelAdmin):
    form = UniversityAdminForm
    list_display = ['name', 'created', 'last_updated', 'scholarship_availability', 'description', 'university_type', 'cost', 'how_to_apply', 'on_campus_housing', 'campusview', 'geolocation', 'application_deadline', 'logo', 'pre_univ']
    readonly_fields = ['slug', 'created', 'last_updated',]

admin.site.register(University, UniversityAdmin)


class ScholarshipAdminForm(forms.ModelForm):

    class Meta:
        model = Scholarship
        fields = '__all__'


class ScholarshipAdmin(admin.ModelAdmin):
    form = ScholarshipAdminForm
    list_display = ['name', 'created', 'last_updated', 'type', 'study_level', 'description', 'application_deadline', 'logo']
    readonly_fields = ['slug','created', 'last_updated',]

admin.site.register(Scholarship, ScholarshipAdmin)


class programAdminForm(forms.ModelForm):

    class Meta:
        model = program
        fields = '__all__'


class programAdmin(admin.ModelAdmin):
    form = programAdminForm
    list_display = ['name', 'created', 'last_updated', 'description']
    readonly_fields = ['slug', 'created', 'last_updated']

admin.site.register(program, programAdmin)


class CountryAdminForm(forms.ModelForm):

    class Meta:
        model = Country
        fields = '__all__'


class CountryAdmin(admin.ModelAdmin):
    form = CountryAdminForm
    list_display = ['name', 'created', 'last_updated', 'continent']
    readonly_fields = ['slug', 'created', 'last_updated']

admin.site.register(Country, CountryAdmin)
