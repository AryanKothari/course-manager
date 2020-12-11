from django.contrib.auth.models import AbstractUser
from django.db import models
from multiselectfield import MultiSelectField



class Course(models.Model):

    DAYS_OF_WEEK_CHOICES = (
    ('MON', 'Monday'),
    ('TUE', 'Tuesday'),
    ('WED', 'Wednesday'),
    ('THU', 'Thursday'),
    ('FRI', 'Friday'),
)
    title = models.CharField(max_length=64, unique=True)
    description = models.TextField()
    professor = models.CharField(max_length=100)
    day  = MultiSelectField(choices=DAYS_OF_WEEK_CHOICES)
    subject = models.CharField(max_length=100, blank=False)
    start_time = models.TimeField(blank=False, default='4:44')
    end_time = models.TimeField(blank=False, default='4:44')
    creation_date = models.DateTimeField(auto_now_add = True, editable=False)

    def __str__(self):
        return f"{self.title} by {self.professor}"
    
    class Meta:
       ordering = ('-creation_date',)

class User(AbstractUser):
    course = models.ManyToManyField(Course)

