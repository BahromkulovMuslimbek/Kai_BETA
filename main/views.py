from django.shortcuts import render, redirect, get_object_or_404
from . import models


def main(request):
    staff_list = models.Staff.objects.all()
    return render(request, 'index.html', {'staff_list': staff_list})


def staff_create(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        age = request.POST.get('age')
        address = request.POST.get('address')
        models.Staff.objects.create(first_name=first_name, last_name=last_name, phone=phone, age=age, address=address)
        return redirect('main')
    return render(request, 'crud/staff/staff_form.html')


def staff_edit(request, pk):
    staff = get_object_or_404(models.Staff, pk=pk)
    if request.method == 'POST':
        staff.first_name = request.POST.get('first_name')
        staff.last_name = request.POST.get('last_name')
        staff.phone = request.POST.get('phone')
        staff.age = request.POST.get('age')
        staff.address = request.POST.get('address')
        staff.save()
        return redirect('main')
    return render(request, 'crud/staff/staff_form.html', {'staff': staff})


def staff_delete(request, pk):
    staff = get_object_or_404(models.Staff, pk=pk)
    if request.method == 'POST':
        staff.delete()
        return redirect('main')
    return render(request, 'crud/staff/staff_confirm_delete.html', {'staff': staff})


def shift_list(request):
    shift_list = models.Shift.objects.all()
    return render(request, 'crud/shift/shift_list.html', {'shift_list': shift_list})


def shift_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        models.Shift.objects.create(name=name, start_time=start_time, end_time=end_time)
        return redirect('shift_list')
    return render(request, 'crud/shift/shift_form.html')


def shift_edit(request, pk):
    shift = get_object_or_404(models.Shift, pk=pk)
    if request.method == 'POST':
        shift.name = request.POST.get('name')
        shift.start_time = request.POST.get('start_time')
        shift.end_time = request.POST.get('end_time')
        shift.save()
        return redirect('shift_list')
    return render(request, 'crud/shift/shift_form.html', {'shift': shift})


def shift_delete(request, pk):
    shift = get_object_or_404(models.Shift, pk=pk)
    if request.method == 'POST':
        shift.delete()
        return redirect('shift_list')
    return render(request, 'crud/shift/shift_confirm_delete.html', {'shift': shift})


def staffshift_list(request):
    staffshift_list = models.StaffShift.objects.all()
    return render(request, 'crud/staffshift/staffshift_list.html', {'staffshift_list': staffshift_list})


def staffshift_create(request):
    if request.method == 'POST':
        staff_id = request.POST.get('staff')
        shift_id = request.POST.get('shift')
        staff = get_object_or_404(models.Staff, id=staff_id)
        shift = get_object_or_404(models.Shift, id=shift_id)
        models.StaffShift.objects.create(staff=staff, shift=shift)
        return redirect('staffshift_list')
    staff_list = models.Staff.objects.all()
    shift_list = models.Shift.objects.all()
    return render(request, 'crud/staffshift/staffshift_form.html', {'staff_list': staff_list, 'shift_list': shift_list})


def staffshift_edit(request, pk):
    staffshift = get_object_or_404(models.StaffShift, pk=pk)
    if request.method == 'POST':
        staff_id = request.POST.get('staff')
        shift_id = request.POST.get('shift')
        staffshift.staff = get_object_or_404(models.Staff, id=staff_id)
        staffshift.shift = get_object_or_404(models.Shift, id=shift_id)
        staffshift.save()
        return redirect('staffshift_list')
    staff_list = models.Staff.objects.all()
    shift_list = models.Shift.objects.all()
    return render(request, 'crud/staffshift/staffshift_form.html', {'staffshift': staffshift, 'staff_list': staff_list, 'shift_list': shift_list})


def staffshift_delete(request, pk):
    staffshift = get_object_or_404(models.StaffShift, pk=pk)
    if request.method == 'POST':
        staffshift.delete()
        return redirect('staffshift_list')
    return render(request, 'crud/staffshift/staffshift_confirm_delete.html', {'staffshift': staffshift})


def position_list(request):
    positions = models.Position.objects.all()
    return render(request, 'crud/position/position_list.html', {'positions': positions})


def position_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        models.Position.objects.create(name=name)
        return redirect('position_list')
    return render(request, 'crud/position/position_form.html')


def position_edit(request, pk):
    position = get_object_or_404(models.Position, pk=pk)
    if request.method == 'POST':
        position.name = request.POST.get('name')
        position.save()
        return redirect('position_list')
    return render(request, 'crud/position/position_form.html', {'position': position})


def position_delete(request, pk):
    position = get_object_or_404(models.Position, pk=pk)
    if request.method == 'POST':
        position.delete()
        return redirect('position_list')
    return render(request, 'crud/position/position_confirm_delete.html', {'position': position})



def attendance_list(request):
    attendance_list = models.StaffAttendance.objects.all()
    return render(request, 'crud/attendance_list.html', {'attendance_list': attendance_list})
