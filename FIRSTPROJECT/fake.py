import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FIRSTPROJECT.settings')

from FIRSTAPPLICATION.models import Name, Contact, Address
from faker import Faker

import django
django.setup()

fake_gen = Faker()


def populate(n):
    for entry in range(n):
        fake_id = fake_gen.numerify('##')
        fake_name = fake_gen.name()

        nme = Name.objects.get_or_create(name_id=fake_id, name=fake_name)[0]

        fake_phn = fake_gen.phone_number()
        fake_url = fake_gen.url()

        cont = Contact.objects.get_or_create(name_id=nme, phn_num=fake_phn, url=fake_url)[0]

        fake_add = fake_gen.address()

        add_r = Address.objects.get_or_create(details=cont, addr=fake_add)


if __name__ == '__main__':
    print("Hello I am populating the Script")
    populate(20)
    print("Populating is done Successfully")



