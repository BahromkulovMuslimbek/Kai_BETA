from django.contrib import admin
from . import models


admin.site.register(models.Position)
admin.site.register(models.Staff)
admin.site.register(models.Shift)
admin.site.register(models.StaffShift)
admin.site.register(models.StaffAttendance)