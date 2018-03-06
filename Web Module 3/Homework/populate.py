import mlab
from models.service import Service
from random import randint, choice
from faker import Faker

mlab.connect()

fake = Faker()

x = ["Ngoan Hien", "Le phep", "De thuong", "Ca tinh", "Chanh cho", "Dam dang"]
y = ["90-60-90", "60-90-60", "69-96-69", "96-69-96"]
z = ['https://images.pexels.com/photos/356378/pexels-photo-356378.jpeg?w=1260&h=750&dpr=2&auto=compress&cs=tinysrgb', 'https://images.pexels.com/photos/8700/wall-animal-dog-pet.jpg?w=1260&h=750&dpr=2&auto=compress&cs=tinysrgb', 'https://images.pexels.com/photos/37401/dog-cute-pet.jpg?w=1260&h=750&dpr=2&auto=compress&cs=tinysrgb', 'https://images.pexels.com/photos/115526/pexels-photo-115526.jpeg?w=1260&h=750&dpr=2&auto=compress&cs=tinysrgb']

for i in range(20):
    print("Saving Service ", i + 1, "....")
    service = Service(name=fake.name(),
                        yob=randint(1990, 2000),
                        gender=randint(0,1),
                        height=randint(150,180),
                        phone=fake.phone_number(),
                        address=fake.address(),
                        status=choice([True, False]),
                        description=choice(x),
                        photo=choice(z),
                        measurement=choice(y))



    service.save()

# print(fake.phone_number())
