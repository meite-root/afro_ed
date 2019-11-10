from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.contrib.postgres.fields import JSONField
from django.db.models import BooleanField
from django.db.models import CharField
from django.db.models import DateTimeField
from django.db.models import ImageField
from django.db.models import IntegerField
from django.db.models import TextField
from django_extensions.db.fields import AutoSlugField
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields
from django.utils.translation import gettext_lazy as _ # For translating
from boards.models import User



class University(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    scholarship_availability = models.CharField(max_length=100, choices=(("none", "None"), ("merit-based", "Merit-based"), ("need-based", "Need-based")))
    description = models.TextField(max_length=1000)
    university_type = models.CharField(max_length=100, choices=(("private", "Private"),("public", "Public")))
    cost = models.IntegerField()
    how_to_apply = models.TextField(max_length=500)
    on_campus_housing = models.BooleanField()
    campusview = models.ImageField(upload_to="upload/images/")
    geolocation = models.TextField(max_length=1000) #JSONField()
    application_deadline = models.DateTimeField()
    logo = models.ImageField(upload_to="upload/images/")
    pre_univ = models.BooleanField()

    def __str__(self):
        return self.name
    # Relationship Fields
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE, related_name="universities",
    )
    programs_offered = models.ManyToManyField(
        'afro_app.program',
        related_name="universities",
    )
    location = models.OneToOneField(
        'afro_app.Country',
        on_delete=models.CASCADE, related_name="universities",
    )

    class Meta:
        ordering = ('-created',)
        verbose_name=_('University')
        verbose_name_plural =_('universities')

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('afro_app_university_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('afro_app_university_update', args=(self.slug,))


class Scholarship(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    type = models.TextField(max_length=100, choices=(("research scholarship", "Research scholarship"), ("study scholarship", "Study scholarship")))
    study_level = models.TextField(max_length=100, choices=(("undergraduate", "Undergraduate"), ("master", "Master"), ("doctorate", "Doctorate")))
    description = models.TextField(max_length=1000)
    application_deadline = models.DateTimeField()
    logo = models.ImageField(upload_to="upload/images/")

    def __str__(self):
        return self.name

    # Relationship Fields
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE, related_name="scholarships",
    )
    programs_applicable = models.ManyToManyField(
        'afro_app.program',
        related_name="scholarships",
    )
    eligible_nationalities = models.ManyToManyField(
        'afro_app.Country',
        related_name="scholarships",
    )
    university_applicable = models.ManyToManyField(
        'afro_app.University',
        related_name="scholarships",
    )

    class Meta:
        ordering = ('-created',)
        verbose_name=_('scholarship')
        verbose_name_plural =_('scholarships')


    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('afro_app_scholarship_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('afro_app_scholarship_update', args=(self.slug,))


class program(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-created',)
        verbose_name=_('Program')
        verbose_name_plural =_('Programs')


    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('afro_app_program_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('afro_app_program_update', args=(self.slug,))


class Country(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    continent = models.TextField(max_length=100, choices=(("asia", "Asia"), ("africa", "Africa"), ("north America", "North America"), ("south America", "South America"), ("australia", "Australia"), ("europe", "Europe")))

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-created',)
        verbose_name=_('Country')
        verbose_name_plural =_('Countries')

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('afro_app_country_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('afro_app_country_update', args=(self.slug,))
