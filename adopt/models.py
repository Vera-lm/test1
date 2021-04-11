from django.db import models
from django.utils.translation import gettext


class Sighting(models.Model):
    Longitude  = models.FloatField(
            help_text = gettext('Longitude of the sight'),
            max_length=30,
            )

    Latitude = models.FloatField(
            help_text = gettext('Latitude of the sight'),
            max_length=30,
            )

    Unique_Squirrel_ID = models.CharField(
            help_text = gettext('The unique ID of the squirrel'),
            max_length = 30,
            )
    
    Shift = models.CharField(
            help_text = gettext('AM or PM'),
            max_length = 2,
            choices = (("AM", "AM"), ("PM", "PM")),
            default = "AM")
    
    Date = models.DateField(
            help_text = _('Date sighted. The format is in mmddyyyy'),
            null = True,
            blank = True,
            default = None,
            )

    Shift = models.CharField(
            help_text = _('Whether the sight is in the morning or late afternoon?'),
            max_length=16,
            choices=SESSION,
            blank=True)

    Date = models.DateField(
            help_text = _('The format is in yyyy-mm-dd'),
            null = True,
            blank=True)
    
    Age = models.CharField(
            help_text = _('Adult or Juvenile'),
            choices = (('Adult','Adult'), ('Juvenile', 'Juvenile'), (None, ''), ('?', '?'),),
            blank = True,
            default = '',
            )

    Primary_Fur_Color = models.CharField(
            help_text = _('Fur color'),
            max_length = 16,
            choices = (('Black', 'Black'), ('Gray', 'Gray'), ('Cinnamon', 'Cinnamon'), (None, ''),),
            blank = True
            )
    
    Location = models.CharField(
            help_text = _('Location'),
            choices = (('Ground Plane', 'Ground Plane'), ('Above Ground', 'Above Ground'), (None, ''),),
            blank = True
            )

    Specific_Location = models.CharField(
            help_text = _('Specific location'),
            blank = True,
            )

    Running = models.NullBooleanField(
            help_text = _('Running'),
            blank=True,
    )
    
    Chasing = models.NullBooleanField(
            help_text = _('Chasing'),
            blank=True,
    )

    Climbing = models.NullBooleanField(
            help_text = _('Climbing'),
            blank=True,
    )

    Eating = models.NullBooleanField(
            help_text = _('Eating'),
            blank=True,
    )

    Foraging = models.NullBooleanField(
            help_text = _('Foraging'),
            blank=True,
    )

    Other_Activities = models.CharField(
        help_text = _('Other Activities'),
        null = True,
        blank = True
    )

    Kuks = models.NullBooleanField(
            help_text = _('Kuks'),
            blank=True,
    )

    Quaas = models.NullBooleanField(
            help_text = _('Quaas'),
            blank=True,
    )

    Moans = models.NullBooleanField(
            help_text = _('Moans'),
            blank=True,
    )

    Tail_flags = models.NullBooleanField(
            help_text = _('Tail flags'),
            blank=True,
    )

    Tail_twitches = models.NullBooleanField(
            help_text = _('Tail twitches'),
            blank=True,
    )

    Approaches = models.NullBooleanField(
            help_text = _('Approaches'),
            blank=True,
    )

    Indifferent = models.NullBooleanField(
            help_text = _('Indifferent'),
            blank=True,
    )
    
    Runs_from = models.NullBooleanField(
            help_text = _('Runs_From'),
            blank=True,
    )

