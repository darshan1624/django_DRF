from django.core.management.base import BaseCommand
from api.models import Student
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Populate the Student model with dummy data'

    def handle(self, *args, **kwargs):
        fake = Faker()
        passby_list = ['Newton', 'Jagddish', 'RajGopal', 'Surve']

        new_students = [
            Student(
                name=fake.name(),
                roll=fake.unique.random_int(min=110, max=200),
                city=fake.city(),
                passby=random.choice(passby_list)
            )
            for _ in range(40)
        ]

        Student.objects.bulk_create(new_students)
        self.stdout.write(self.style.SUCCESS('Dummy data inserted successfully!'))
