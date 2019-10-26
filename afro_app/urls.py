from django.urls import path, include
from rest_framework import routers

from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'university', api.UniversityViewSet)
router.register(r'scholarship', api.ScholarshipViewSet)
router.register(r'program', api.programViewSet)
router.register(r'country', api.CountryViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path('api/v1/', include(router.urls)),
)


urlpatterns += (
    # urls for University
    path('university/', views.UniversityListView.as_view(), name='afro_app_university_list'),
    path('university/create/', views.UniversityCreateView.as_view(), name='afro_app_university_create'),
    path('university/detail/<slug:slug>/', views.UniversityDetailView.as_view(), name='afro_app_university_detail'),
    path('university/update/<slug:slug>/', views.UniversityUpdateView.as_view(), name='afro_app_university_update'),
)

urlpatterns += (
    # urls for Scholarship
    path('scholarship/', views.ScholarshipListView.as_view(), name='afro_app_scholarship_list'),
    path('scholarship/create/', views.ScholarshipCreateView.as_view(), name='afro_app_scholarship_create'),
    path('scholarship/detail/<slug:slug>/', views.ScholarshipDetailView.as_view(), name='afro_app_scholarship_detail'),
    path('scholarship/update/<slug:slug>/', views.ScholarshipUpdateView.as_view(), name='afro_app_scholarship_update'),
)

urlpatterns += (
    # urls for program
    path('program/', views.programListView.as_view(), name='afro_app_program_list'),
    path('program/create/', views.programCreateView.as_view(), name='afro_app_program_create'),
    path('program/detail/<slug:slug>/', views.programDetailView.as_view(), name='afro_app_program_detail'),
    path('program/update/<slug:slug>/', views.programUpdateView.as_view(), name='afro_app_program_update'),
)

urlpatterns += (
    # urls for Country
    path('country/', views.CountryListView.as_view(), name='afro_app_country_list'),
    path('country/create/', views.CountryCreateView.as_view(), name='afro_app_country_create'),
    path('country/detail/<slug:slug>/', views.CountryDetailView.as_view(), name='afro_app_country_detail'),
    path('country/update/<slug:slug>/', views.CountryUpdateView.as_view(), name='afro_app_country_update'),
)
