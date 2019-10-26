from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import University, Scholarship, program, Country
from .forms import UserForm, UniversityForm, ScholarshipForm, programForm, CountryForm

# Universities
class UniversityListView(ListView):
    model = University


class UniversityCreateView(CreateView):
    model = University
    form_class = UniversityForm


class UniversityDetailView(DetailView):
    model = University


class UniversityUpdateView(UpdateView):
    model = University
    form_class = UniversityForm


# Scholarships
class ScholarshipListView(ListView):
    model = Scholarship


class ScholarshipCreateView(CreateView):
    model = Scholarship
    form_class = ScholarshipForm


class ScholarshipDetailView(DetailView):
    model = Scholarship


class ScholarshipUpdateView(UpdateView):
    model = Scholarship
    form_class = ScholarshipForm



# Programs
class programListView(ListView):
    model = program


class programCreateView(CreateView):
    model = program
    form_class = programForm


class programDetailView(DetailView):
    model = program


class programUpdateView(UpdateView):
    model = program
    form_class = programForm


#Countries
class CountryListView(ListView):
    model = Country


class CountryCreateView(CreateView):
    model = Country
    form_class = CountryForm


class CountryDetailView(DetailView):
    model = Country


class CountryUpdateView(UpdateView):
    model = Country
    form_class = CountryForm
