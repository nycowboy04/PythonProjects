import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

import random
from faker import Faker
from AppTwo.models import User
fakegen=Faker()

def populate(N=5):
    for item in range(N):
        fake_first=fakegen.first_name()
        fake_last=fakegen.last_name()
        fake_email=fakegen.email()

        usr=User.objects.get_or_create(first_name=fake_first, last_name=fake_last, email=fake_email)

if __name__=='__main__':
    print("populating database!")
    populate(20)
    print("population complete!")
