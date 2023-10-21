from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

# Documentation: https://docs.djangoproject.com/en/4.2/ref/models/fields/#django.db.models.Field

class User(AbstractUser):
    pass


class Lead(models.Model):
    SOURCE_CHOICES = (
        # First value is the actual value stored in the database, second value is the display value
        ('YT', 'YouTube'),
        ('GOOGLE', 'Google'),
        ('NEWSLETTER', 'Newsletter'),
    )

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)

    # phoned = models.BooleanField(default=False)
    # # blank=True means that the field is not required. Source = youtube, twitter, etc.
    # # choices=SOURCE_CHOICES means that the field can only be one of the values in SOURCE_CHOICES
    # source = models.CharField(choices=SOURCE_CHOICES, max_length=100)

    # # blank=True means that the field is not required, null=True means that the field can be null
    # profile_picture = models.ImageField(blank=True, null=True)
    # special_files = models.FileField(blank=True, null=True)

    # FOREIGN KEY RELATIONSHIP
    # agent = models.ForeignKey("Agent", on_delete=models.SET_NULL, null=True,default="abc") #set null means that if the agent is deleted, the lead will not be deleted, but the agent field will be set to null

    agents = models.ForeignKey("Agent", on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Agent is a user, so we can use the built-in user model, one-to-one relationship


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
