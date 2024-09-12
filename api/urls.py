from django.urls import path
from .views import (
    StaffListCreateAPIView, StaffRetrieveUpdateDestroyAPIView, ShiftListCreateAPIView, ShiftRetrieveUpdateDestroyAPIView, PositionListCreateAPIView, PositionRetrieveUpdateDestroyAPIView, 
    StaffShiftListCreateAPIView, StaffShiftRetrieveUpdateAPIView, StaffAttendanceListCreateAPIView, StaffAttendanceRetrieveAPIView
)

urlpatterns = [
    path('staff/', StaffListCreateAPIView.as_view(), name='staff-list-create'),
    path('staff/<int:pk>/', StaffRetrieveUpdateDestroyAPIView.as_view(), name='staff-detail'),

    path('shift/', ShiftListCreateAPIView.as_view(), name='shift-list-create'),
    path('shift/<int:pk>/', ShiftRetrieveUpdateDestroyAPIView.as_view(), name='shift-detail'),

    path('position/', PositionListCreateAPIView.as_view(), name='position-list-create'),
    path('position/<int:pk>/', PositionRetrieveUpdateDestroyAPIView.as_view(), name='position-detail'),

    path('staff-shift/', StaffShiftListCreateAPIView.as_view(), name='staff-shift-list-create'),
    path('staff-shift/<int:pk>/', StaffShiftRetrieveUpdateAPIView.as_view(), name='staff-shift-detail'),

    path('staff-attendance/', StaffAttendanceListCreateAPIView.as_view(), name='staff-attendance-list-create'),
    path('staff-attendance/<int:pk>/', StaffAttendanceRetrieveAPIView.as_view(), name='staff-attendance-detail'),

]

