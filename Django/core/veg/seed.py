from faker import Faker
from veg.models import *
import random
faker = Faker()

def seed_db(n=10)->None :
    for i in range(0,200):
        student_email =  faker.email()
        student_age= random.randint(18 , 30)
        student_address = faker.address()
        student_name = faker.name()
        department_obj = Department.objects.all() # This is a QuerySet
        if not department_obj.exists():
            print("No departments found in the database. Please create some departments first.")
            return
        # random.choice is the preferred way to select a random element from a sequence.
        department = random.choice(department_obj)
        student_id = f"0108SATI{department}{random.randint(100,999)}"

        student_id_obj= StudentID.objects.create(student_id = student_id)
      
        Student.objects.create(
            student_email =student_email,
            student_age = student_age,
            student_address =student_address,
            student_name = student_name,
            department = department,
            student_id = student_id_obj
        )
