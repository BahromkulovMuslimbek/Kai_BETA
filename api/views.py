from rest_framework import generics
from main.models import Staff, Shift, Position, StaffShift, StaffAttendance
from .serializers import StaffSerializer, ShiftSerializer, PositionSerializer, StaffShiftSerializer, StaffAttendanceSerializer


class StaffListCreateAPIView(generics.ListCreateAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer


class StaffRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer


class ShiftListCreateAPIView(generics.ListCreateAPIView):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer


class ShiftRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer


class PositionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class PositionRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class StaffShiftListCreateAPIView(generics.ListCreateAPIView):
    queryset = StaffShift.objects.all()
    serializer_class = StaffShiftSerializer


class StaffShiftRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StaffShift.objects.all()
    serializer_class = StaffShiftSerializer


class StaffAttendanceListCreateAPIView(generics.ListCreateAPIView):
    queryset = StaffAttendance.objects.all()
    serializer_class = StaffAttendanceSerializer


class StaffAttendanceRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StaffAttendance.objects.all()
    serializer_class = StaffAttendanceSerializer
