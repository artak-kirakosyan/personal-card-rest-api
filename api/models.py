from django.db import models


class PersonalCard(models.Model):
    class Gender(models.TextChoices):
        MALE = "M", "Male"
        FEMALE = "F", "Female"
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    middle_name = models.CharField(
        max_length=50, blank=True, null=True, default=None
    )
    age = models.PositiveIntegerField(null=False, blank=False)
    gender = models.CharField(
        choices=Gender.choices,
        max_length=1
    )
    vaccinated = models.BooleanField(default=False)

    class Meta:
        ordering = ["last_name", "name", "middle_name"]
