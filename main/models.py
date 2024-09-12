from django.core.validators import RegexValidator
from django.db import models
from django.db.models import Q


class Staff(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=15, unique=True,
        # validators=[RegexValidator(regex=r'^\d{10,15}$', message="Telefonda 10 tadan 15 tagacha raqam bolishi kerak")]
    )
    age = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    @classmethod
    def search_by_name(cls, name):
        return cls.objects.filter(
            Q(first_name__icontains=name) | Q(last_name__icontains=name)
        )


class Shift(models.Model):
    name = models.CharField(max_length=255)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=255)
    staff = models.OneToOneField(Staff, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name
    

class StaffShift(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('staff', 'shift')

    def __str__(self):
        return f"{self.staff} - {self.shift}"
    

class StaffAttendance(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    date_time = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=255, choices=[('Present', 'Present'), ('Absent', 'Absent')])

    class Meta:
        unique_together = ('staff', 'date_time')

    def __str__(self):
        return f"{self.staff} - {self.date_time} - {self.status}"