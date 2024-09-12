from . import models

def create_datas():
    staff_1 = models.Staff.objects.create(first_name='Ali', last_name='Boboyev', phone='998907772233', age=30, address='Qoqon')
    staff_2 = models.Staff.objects.create(first_name='Husan', last_name='Davlatov', phone='998903337711', age=25, address='Quva')
    staff_3 = models.Staff.objects.create(first_name='Elmurod', last_name='Rahimov', phone='998906661122', age=28, address='Rishton')
    staff_4 = models.Staff.objects.create(first_name='Jahongir', last_name='Dadajonov', phone='998337772233', age=19, address='Namangan')
    staff_5 = models.Staff.objects.create(first_name='Islom', last_name='Ibragimov', phone='998911112233', age=32, address='Andijon')

    
    print(f"Created: {staff_1}, {staff_2}, {staff_3}, {staff_4, {staff_5}}")

