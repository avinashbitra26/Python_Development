import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

import django
django.setup()

import random
from faker import Faker
from first_app.models import Webpage, Topic, AccessRecord

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']


def add_topic():
    d = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    d.save()
    return d


def populate(N):
    for i in range(N):
        # get the topic for entry
        top = add_topic()

        # create fake data for the entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # create the new webpage entry
        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        # create fake access record for webpage
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]


if __name__ == '__main__':
    print("populating the data")
    populate(25)
    print("populated the data")
