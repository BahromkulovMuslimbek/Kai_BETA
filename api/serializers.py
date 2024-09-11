from rest_framework import serializers
from main.models import Staff, Shift, Position, StaffShift, StaffAttendance


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'


class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shift
        fields = '__all__'


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'


class StaffShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffShift
        fields = '__all__'


class StaffAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffAttendance
        fields = '__all__'