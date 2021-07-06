import os
import random

import django
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Library_Management.settings')
django.setup()

from library.models import *

"""
Used to insert Fake data into Model
"""


def populate_data():
    fake = Faker()
    Faker.seed(0)
    random.seed(0)
    books = ['Physics', 'Chemistry', 'Maths', 'English']
    for i in range(100):
        name = fake.name()
        pid = fake.numerify(text='######')
        email = fake.email()
        address = fake.address()

        person = Person.objects.get_or_create(pid=pid, name=name, email=email, address=address)[0]

    for i in range(50):
        book = random.choice(books)
        isbn = fake.numerify(text='#############')
        author = fake.name()
        publisher = fake.first_name()

        book = Books.objects.get_or_create(name=book, isbn=isbn, author=author, publisher=publisher)[0]

        # print(book, isbn, author, publisher)


populate_data()
print('DONE!!!!')
