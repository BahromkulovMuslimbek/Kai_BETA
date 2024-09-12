import os
import django
import random
from faker import Faker

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Kai.settings")
django.setup()

from main.models import Staff

fake = Faker()

def create_fake_staff(n):
    for _ in range(n):
        staff = Staff(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            phone=fake.phone_number(),
            age=random.randint(18, 50),
            address=fake.address()
        )
        staff.save()

if __name__ == "__main__":
    print("Starting to populate the database with fake staff data...")
    create_fake_staff(5)
    print("Database populated.")
