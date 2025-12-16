from faker import Faker
from veg.models import *
import random
from django.db.models import Q, Sum
faker = Faker()

def seed_db()->None :
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

def user():
    for _ in range(0,100):
        first_name = faker.first_name()
        last_name = faker.last_name()
        email = faker.email()
        username = faker.user_name()
        password = faker.password()

        # Use create_user() to properly create a user and hash the password.
        User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
def sub_M():
    try:
        student_obj = Student.objects.all()
        for student in student_obj:
            sub_obj = Subject.objects.all()
            for sub in sub_obj:
                Subject_M.objects.create(
                    student = student,
                    subject = sub,
                    marks = random.randint(0 , 100)
                )

    except Exception as e:
        print(e)

def std_rank():
    ranks = Student.objects.annotate(marks=Sum("studentmarks__marks")).order_by("-marks")
    count = 1
    for rank in ranks:
        
        Rank.objects.create(
            student = rank,
            rank_no = count
        )
        count +=1
