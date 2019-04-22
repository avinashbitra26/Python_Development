import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'userinfo.settings')

import django
django.setup()

from first_app.models import User
from faker import Faker

fakegen = Faker()


def populate(N):
    for i in range(N):
        name = fakegen.name().split()
        first_name = name[0]
        last_name = name[1]
        email = fakegen.email()

        # New entry
        user = User.objects.get_or_create(first_name=first_name,
                                          last_name=last_name,
                                          email=email)[0]

if __name__ == '__main__':
    populate(20)
    print("Populated Successfully!")
