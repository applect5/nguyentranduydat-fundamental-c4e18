from models.service import Service
import mlab
from faker import Faker
from random import  randint, choice



mlab.connect()
fake = Faker()

for i in range (1):
    print("Saving service","."*20)
    new_service = Service(
        name=fake.name(),
        yob=randint(1996,2002),
        gender=randint(0,1),
        height=randint(150,170),
        phone=fake.phone_number(),
        address=fake.address(),
        description = choice(['Xinh gái','Dáng ngon','Thông minh sắc xảo','Hài hước']),
        measurements = str([randint(85,95),randint(55,65),randint(85,95)]),
        avatar = 'static/36601356_300117887194720_2666822202850017280_o.jpg'   
    )
    new_service.save()