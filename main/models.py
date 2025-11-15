from django.db import models


class IconChoices(models.TextChoices):
    FLAG = "fa-solid fa-flag", "Flag"
    ALERT = "fa-solid fa-circle-exclamation", "Alert"
    CHECK = "fa-solid fa-check", "Check"


class Priority(models.Model):
    name = models.CharField(max_length=50)
    icon = models.CharField(
        max_length=100,
        choices=IconChoices.choices,
        default=IconChoices.CHECK
    )
    
    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=100)
    execute_time = models.DateField()
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    
class BirthDayEvent(models.Model):
    person_name = models.CharField(max_length=150)
    datetime = models.DateField()
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.person_name
    