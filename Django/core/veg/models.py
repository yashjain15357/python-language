from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Recp(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)  #When the referenced object (e.g., a User) is deleted, all related objects (e.g., Recp recipes) are also deleted automatically.

    recp_name = models.CharField(max_length=100 , null=False)
    recp_decp= models.TextField()
    recp_img = models.ImageField(upload_to="recp")

# view = Post.objects.all().order_by("views")  //ascending
# view = Post.objects.all().order_by("-views") //decending

# posts = Post.objects.filter(views__gte=100).order_by("-views")



# models.CASCADE
# Deletes related objects when the referenced object is deleted.

# models.PROTECT
# Prevents deletion of the referenced object if related objects exist (raises ProtectedError).

# models.SET_NULL
# Sets the foreign key to NULL when the referenced object is deleted (requires null=True).

# models.SET_DEFAULT
# Sets the foreign key to its default value when the referenced object is deleted.

# models.SET()
# Sets the foreign key to the value passed to SET() (e.g., a function or a value).

# models.DO_NOTHING
# Does nothing; you must handle the situation manually.




class Department(models.Model):
    department = models.CharField(max_length=100)

    # Django uses the __str__ method to get a human-readable string representation of an object.
    def __str__(self)-> str:
        return self.department
    
    class Meta:
        # is an option that tells Django what the default ordering should be when you retrieve a list of Department objects from the database.
        ordering = ['department']

class StudentID (models.Model):
   student_id = models.CharField(max_length=100)
   def __str__(self)->str:
      return self.student_id

class Student(models.Model):
   department = models.ForeignKey(Department,related_name='depart', on_delete=models.CASCADE)
   student_id = models.OneToOneField(StudentID , related_name='studentid' ,on_delete=models.CASCADE )
   student_name = models.CharField(max_length=100)
   student_email = models.EmailField(unique=True)
   student_age= models.IntegerField(default=18)
   student_address = models.TextField()

   def __str__(self)->str:
      return self.student_name
   
   class Meta:
      ordering = ['student_name']
      verbose_name = "student"

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)

  def __str__(self):
    return f"{self.firstname} {self.lastname}"
  

# Advance query run 
# from django.db.models import Q, Count, Avg, Sum, F

# Basic Filtering (like your examples)
#   query = Student.objects.filter(student_name__startswith="A")
#   query = Student.objects.filter(student_name__endswith="n")

# Field Lookups (gt, lt, in, range)
#   # Find students older than 21
#   students_over_21 = Student.objects.filter(student_age__gt=21)
#   # Find students with age between 20 and 25 (inclusive)
#   students_in_range = Student.objects.filter(student_age__range=(20, 25))


# "Spanning Relationships" is a powerful feature of the Django ORM that lets you write queries that "cross over" from one model to another through their defined relationships (ForeignKey, OneToOneField, ManyToManyField).

# Spanning Relationships (Querying across ForeignKeys)
#   # Find all students in the 'Computer Science' department
#   cs_students = Student.objects.filter(department__department="Computer Science")
#   # Find all students with a specific Student ID string
#   student_by_id_str = Student.objects.filter(student_id__student_id="0108SATICS123")

# Complex queries with Q objects (for OR, AND, NOT logic)
#   # Find students whose name starts with 'A' OR are older than 25
#   query = Student.objects.filter(Q(student_name__startswith='A') | Q(student_age__gt=25))
#   # Find students in the 'Computer Science' department AND whose name contains 'jain'
#   query = Student.objects.filter(Q(department__department="Computer Science") & Q(student_name__icontains='jain'))

# Excluding objects
#   # Get all students EXCEPT those in the 'Mechanical' department
#   non_mech_students = Student.objects.exclude(department__department="Mechanical")

# Annotation (adding a calculated field to each object in the queryset)
#   # Get each Department and add a count of how many students are in it
#   depts_with_student_counts = Department.objects.annotate(num_students=Count('depart'))
#   # You can then access it like: for dept in depts_with_student_counts: print(dept.department, dept.num_students)

# Aggregation (calculating a summary value for the entire queryset)
#   # Get the average age of all students
#   avg_age = Student.objects.aggregate(average_age=Avg('student_age')) # Returns a dictionary: {'average_age': 22.5}
#   # Get the total number of recipes
#   total_recipes = Recp.objects.aggregate(total=Count('id')) # Returns {'total': 50}