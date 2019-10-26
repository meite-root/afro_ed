import unittest
from django.urls import reverse
from django.test import Client
from .models import User, University, Scholarship, program, Country
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_university(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["scholarship_availability"] = "scholarship_availability"
    defaults["description"] = "description"
    defaults["university_type"] = "university_type"
    defaults["cost"] = "cost"
    defaults["how_to_apply"] = "how_to_apply"
    defaults["on_campus_housing"] = "on_campus_housing"
    defaults["campusview"] = "campusview"
    defaults["geolocation"] = "geolocation"
    defaults["application_deadline"] = "application_deadline"
    defaults["logo"] = "logo"
    defaults["pre_univ"] = "pre_univ"
    defaults.update(**kwargs)
    if "author" not in defaults:
        defaults["author"] = create_user()
    if "programs_offered" not in defaults:
        defaults["programs_offered"] = create_program()
    if "location" not in defaults:
        defaults["location"] = create_country()
    return University.objects.create(**defaults)


def create_scholarship(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["type"] = "type"
    defaults["study_level"] = "study_level"
    defaults["description"] = "description"
    defaults["application_deadline"] = "application_deadline"
    defaults["logo"] = "logo"
    defaults.update(**kwargs)
    if "author" not in defaults:
        defaults["author"] = create_user()
    if "programs_applicable" not in defaults:
        defaults["programs_applicable"] = create_program()
    if "eligible_nationalities" not in defaults:
        defaults["eligible_nationalities"] = create_country()
    if "university_applicable" not in defaults:
        defaults["university_applicable"] = create_university()
    return Scholarship.objects.create(**defaults)


def create_program(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["description"] = "description"
    defaults.update(**kwargs)
    return program.objects.create(**defaults)


def create_country(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["continent"] = "continent"
    defaults.update(**kwargs)
    return Country.objects.create(**defaults)


class UserViewTest(unittest.TestCase):
    '''
    Tests for User
    '''
    def setUp(self):
        self.client = Client()

    def test_list_user(self):
        url = reverse('afro_app_user_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_user(self):
        url = reverse('afro_app_user_create')
        data = {
            "username": "username",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_user(self):
        user = create_user()
        url = reverse('afro_app_user_detail', args=[user.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_user(self):
        user = create_user()
        data = {
            "username": "username",
        }
        url = reverse('afro_app_user_update', args=[user.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class UniversityViewTest(unittest.TestCase):
    '''
    Tests for University
    '''
    def setUp(self):
        self.client = Client()

    def test_list_university(self):
        url = reverse('afro_app_university_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_university(self):
        url = reverse('afro_app_university_create')
        data = {
            "name": "name",
            "scholarship_availability": "scholarship_availability",
            "description": "description",
            "university_type": "university_type",
            "cost": "cost",
            "how_to_apply": "how_to_apply",
            "on_campus_housing": "on_campus_housing",
            "campusview": "campusview",
            "geolocation": "geolocation",
            "application_deadline": "application_deadline",
            "logo": "logo",
            "pre_univ": "pre_univ",
            "author": create_user().pk,
            "programs_offered": create_program().pk,
            "location": create_country().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_university(self):
        university = create_university()
        url = reverse('afro_app_university_detail', args=[university.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_university(self):
        university = create_university()
        data = {
            "name": "name",
            "scholarship_availability": "scholarship_availability",
            "description": "description",
            "university_type": "university_type",
            "cost": "cost",
            "how_to_apply": "how_to_apply",
            "on_campus_housing": "on_campus_housing",
            "campusview": "campusview",
            "geolocation": "geolocation",
            "application_deadline": "application_deadline",
            "logo": "logo",
            "pre_univ": "pre_univ",
            "author": create_user().pk,
            "programs_offered": create_program().pk,
            "location": create_country().pk,
        }
        url = reverse('afro_app_university_update', args=[university.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ScholarshipViewTest(unittest.TestCase):
    '''
    Tests for Scholarship
    '''
    def setUp(self):
        self.client = Client()

    def test_list_scholarship(self):
        url = reverse('afro_app_scholarship_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_scholarship(self):
        url = reverse('afro_app_scholarship_create')
        data = {
            "name": "name",
            "type": "type",
            "study_level": "study_level",
            "description": "description",
            "application_deadline": "application_deadline",
            "logo": "logo",
            "author": create_user().pk,
            "programs_applicable": create_program().pk,
            "eligible_nationalities": create_country().pk,
            "university_applicable": create_university().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_scholarship(self):
        scholarship = create_scholarship()
        url = reverse('afro_app_scholarship_detail', args=[scholarship.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_scholarship(self):
        scholarship = create_scholarship()
        data = {
            "name": "name",
            "type": "type",
            "study_level": "study_level",
            "description": "description",
            "application_deadline": "application_deadline",
            "logo": "logo",
            "author": create_user().pk,
            "programs_applicable": create_program().pk,
            "eligible_nationalities": create_country().pk,
            "university_applicable": create_university().pk,
        }
        url = reverse('afro_app_scholarship_update', args=[scholarship.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class programViewTest(unittest.TestCase):
    '''
    Tests for program
    '''
    def setUp(self):
        self.client = Client()

    def test_list_program(self):
        url = reverse('afro_app_program_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_program(self):
        url = reverse('afro_app_program_create')
        data = {
            "name": "name",
            "description": "description",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_program(self):
        program = create_program()
        url = reverse('afro_app_program_detail', args=[program.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_program(self):
        program = create_program()
        data = {
            "name": "name",
            "description": "description",
        }
        url = reverse('afro_app_program_update', args=[program.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class CountryViewTest(unittest.TestCase):
    '''
    Tests for Country
    '''
    def setUp(self):
        self.client = Client()

    def test_list_country(self):
        url = reverse('afro_app_country_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_country(self):
        url = reverse('afro_app_country_create')
        data = {
            "name": "name",
            "continent": "continent",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_country(self):
        country = create_country()
        url = reverse('afro_app_country_detail', args=[country.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_country(self):
        country = create_country()
        data = {
            "name": "name",
            "continent": "continent",
        }
        url = reverse('afro_app_country_update', args=[country.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


