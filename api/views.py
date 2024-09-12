from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.mixins import LoginRequiredMixin
from main.models import Staff, Shift, Position, StaffShift, StaffAttendance
from .serializers import StaffSerializer, ShiftSerializer, PositionSerializer, StaffShiftSerializer, StaffAttendanceSerializer


class StaffListCreateAPIView(generics.ListCreateAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    permission_classes = [IsAdminUser]


class StaffRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView, LoginRequiredMixin):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    permission_classes = [IsAuthenticated]


class PositionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    permission_classes = [IsAdminUser] 

class PositionRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView, LoginRequiredMixin):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend] 


class ShiftListCreateAPIView(generics.ListCreateAPIView):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer
    permission_classes = [IsAdminUser] 

class ShiftRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer
    permission_classes = [IsAdminUser] 


class StaffShiftListCreateAPIView(generics.ListCreateAPIView):
    queryset = StaffShift.objects.all()
    serializer_class = StaffShiftSerializer
    permission_classes = [IsAdminUser]

class StaffShiftRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView, LoginRequiredMixin):
    queryset = StaffShift.objects.all()
    serializer_class = StaffShiftSerializer
    permission_classes = [IsAuthenticated]


class StaffAttendanceListCreateAPIView(generics.ListCreateAPIView, LoginRequiredMixin):
    queryset = StaffAttendance.objects.all()
    serializer_class = StaffAttendanceSerializer
    permission_classes = [IsAuthenticated]


class StaffAttendanceRetrieveAPIView(generics.RetrieveAPIView):
    queryset = StaffAttendance.objects.all()
    serializer_class = StaffAttendanceSerializer
    permission_classes = [IsAdminUser]
