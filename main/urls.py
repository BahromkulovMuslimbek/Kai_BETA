from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='staff_list'),
    path('staff/create/', views.staff_create, name='staff_create'),
    path('staff/<int:pk>/edit/', views.staff_edit, name='staff_edit'),
    path('staff/<int:pk>/delete/', views.staff_delete, name='staff_delete'),

    path('positions/', views.position_list, name='position_list'),
    path('positions/create/', views.position_create, name='position_create'),
    path('positions/<int:pk>/edit/', views.position_edit, name='position_edit'),
    path('positions/<int:pk>/delete/', views.position_delete, name='position_delete'),

    
    path('shift/', views.shift_list, name='shift_list'),
    path('shift/create/', views.shift_create, name='shift_create'),
    path('shift/<int:pk>/edit/', views.shift_edit, name='shift_edit'),
    path('shift/<int:pk>/delete/', views.shift_delete, name='shift_delete'),
    
    path('staffshift/', views.staffshift_list, name='staffshift_list'),
    path('staffshift/create/', views.staffshift_create, name='staffshift_create'),
    path('staffshift/<int:pk>/edit/', views.staffshift_edit, name='staffshift_edit'),
    path('staffshift/<int:pk>/delete/', views.staffshift_delete, name='staffshift_delete'),
    
    path('attendance/', views.attendance_list, name='attendance_list'),

]
