import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','SANKET.settings')

import django 
django.setup()

import random
from sd_app.models import Topic,Webpage, AccessRecord
from faker import Faker

fakegen = Faker()
topics = ['Search','Social','Marketplace','News','Games']

def add_topic():
    t = Topic.objects.get(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):

    for entry in range(N):

        top = add_topic()

        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        wepg = Webpage.objects.get(topic=top,url = fake_url,name=fake_name)[0]

        accc_rec = AccessRecord.objects.get(name= wepg,date=fake_date)[0]

if __name__=='__main__':
    print("populating script")
    populate()
    print("population completed")-