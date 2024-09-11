from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Staff(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Shift(models.Model):
    name = models.CharField(max_length=255)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.name
    

class StaffShift(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)
    shift_date = models.DateField()

    def __str__(self):
        return f"{self.staff} - {self.shift} on {self.shift_date}"
    

class StaffAttendance(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=50, choices=[('Present', 'Present'), ('Absent', 'Absent')])

    def __str__(self):
        return f"{self.staff} - {self.date} - {self.status}"