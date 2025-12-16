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
# Deletes related objects(row) when the referenced object is deleted.

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
    department = models.CharField(max_length=100, primary_key=True)

    # Django uses the __str__ method to get a human-readable string representation of an object.
    def __str__(self)-> str:
        return self.department
    
    class Meta:
        # is an option that tells Django what the default ordering should be when you retrieve a list of Department objects from the database.
        ordering = ['department']

class StudentID (models.Model):
   student_id = models.CharField(max_length=100 , unique=True , primary_key=True)
   def __str__(self)->str:
      return self.student_id

class Student(models.Model):
   department = models.ForeignKey(Department,related_name='depart', on_delete=models.CASCADE)
   student_id = models.OneToOneField(StudentID , related_name='studentid' ,on_delete=models.CASCADE  , primary_key=True)
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

  def __str__(self)->str:
    return f"{self.firstname} {self.lastname}"

class Subject (models.Model):
   subject  = models.CharField(max_length=100)
   def __str__(self):
      return self.subject

class Subject_M(models.Model):
   student = models.ForeignKey(Student, related_name="studentmarks", on_delete= models.CASCADE)
   # student_id = models.ForeignKey(StudentID,related_name='student_id', on_delete=models.CASCADE )
   subject = models.ForeignKey(Subject , on_delete=models.CASCADE)
   marks = models.IntegerField() 
    
   def __str__(self):
      return f'{self.student.student_name} {self.subject.subject}'

   class Meta:
      ordering = ['student']
      unique_together = [['student', 'subject']]


class Rank(models.Model):
   student = models.ForeignKey(Student , related_name='student_rank',on_delete=models.CASCADE)
   rank_no = models.IntegerField(null=False)
   total_marks = models.IntegerField(null=True)
   # date_of_report = models.DateField(auto_now_add=True)


   def __str__(self):
      return f"{self.rank_no} - {self.student.student_name}"







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

#   student_in_dep = ["CSE" , "AIADS"]
#   student_dep = Student.objects.filter(department__department__in = student_in_dep )


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



# Optimizing Queries with .values() and .values_list()
# These methods are used to retrieve only the specific data you need, which can be much more efficient than retrieving full model instances.

# .values(*fields) - Returns a QuerySet of dictionaries.
#   # Get a list of dictionaries, each containing the name and age of a student.
#   student_data = Student.objects.values('student_name', 'student_age')
#   # Result might look like: <QuerySet [{'student_name': 'Yash Jain', 'student_age': 22}, {'student_name': 'Riya Jain', 'student_age': 21}, ...]>

# .values_list(*fields, flat=False) - Returns a QuerySet of tuples.
#   # Get a list of tuples, each containing the id and name of a student.
#   student_tuples = Student.objects.values_list('id', 'student_name')
#   # Result might look like: <QuerySet [(1, 'Yash Jain'), (2, 'Riya Jain'), ...]>

# .values_list() with flat=True
#   # If you only need one field, `flat=True` will give you a simple list of values instead of tuples.
#   student_names_list = Student.objects.values_list('student_name', flat=True)
#   # Result might look like: <QuerySet ['Yash Jain', 'Riya Jain', ...]>




# [
# {'username': 'yash', 'password': 'pbkdf2_sha256$1000000$t9z7Mz1YVu9nAIcxxr50zd$AaRc0d+0L+EFkc2/rjCTm27Ex59hovRwq5/pu7P2M9A=', 'email': 'usj@gmail.com'}, 
# {'username': 'yash jain', 'password': 'pbkdf2_sha256$1000000$GQOfgw47t2MvbVPiUkejQt$2c79qMdV1/RMwDUPjJDbtTwzKSwGDn88iNhtyZnO+Ow=', 'email': 'jainy9089@gmail.com'}, {'username': 'adfsdf', 'password': 'pbkdf2_sha256$1000000$rsWiXQnZ5FQso6bUvb28lP$EUMHwRm/vBgLhzkNw8Q2Sy4lZIZqpped1IuuwbqkKrw=', 'email': 'asdf@gmail.com'}, {'username': 'yash_15357', 'password': 'pbkdf2_sha256$1000000$dzsfIql067HURS8EaakjoN$umyIGgw2kkBMHMMfNp3jZwZj2ryI52/4Fzy8EME2T2Q=', 'email': '123@12'}, {'username': 'yashjain', 'password': 'pbkdf2_sha256$1000000$NGJBrSGe7xXzWB1U9JH9Mb$juDuIWVShK05hGHz7kjUO57S7i2EH203cZDe8vgOrDo=', 'email': 'jainy@gmil.com'}, {'username': 'raksha', 'password': 'pbkdf2_sha256$1000000$XhwQ9uXYXp29Dg0HidLu6C$TTaxw/thGdJOoktedgxbITXA8WgHdtm92tjkdI6XJY0=', 'email': ''}, {'username': 'anjali', 'password': 'pbkdf2_sha256$1000000$inULLIlsriCkOZV0pxv4oS$5kVoHyPycd5oYQrQg10QDDtUAV31M54GOVzZFsFJM1k=', 'email': 'anjali@gmil.com'}, {'username': 'nicholas50', 'password': 'pbkdf2_sha256$1000000$lRAcEeoVLXRIbl0g6P2PKw$NAxk4D0BYw7gK2Rm6p6g/3F3UijrPQ3a4gFzgsFlI3k=', 'email': 'michaelmayer@example.com'}, {'username': 'bcaldwell', 'password': 'pbkdf2_sha256$1000000$e8pcg7nPlxUN19OV17e6Ld$4kO1gPWPr+3lSQthVJhsl1rzqdPtOZaRYmbEZVtL8yg=', 'email': 'bhumphrey@example.net'}, {'username': 'saraburke', 'password': 'pbkdf2_sha256$1000000$rvcuAmONrKMZtLF6gsV2Jj$3fDuwHrg/c0E7sEiqaVznVU5GkUP5jOlMPzv9XeuEHU=', 'email': 'bobbyroth@example.com'}, {'username': 'gomezrussell', 'password': 'pbkdf2_sha256$1000000$9Cs9h42fpr2pGY3wEtjsIs$aKj0I9F2xCaVlSnoFBf9dy0k1NA9IEzgffap+S3cJmc=', 'email': 'thompsongeorge@example.org'}, {'username': 'lewisnancy', 'password': 'pbkdf2_sha256$1000000$UD978U9Q6JsijAArnt0DW6$XlQoNE4aVggRuCrl+5HPn8/197n0q5lQJylgFbz+gUQ=', 'email': 'jason73@example.net'}, {'username': 'masonmichael', 'password': 'pbkdf2_sha256$1000000$MzYEpCKb5ro7qJGjsGc4gM$RBNs4lxsSW0GhQ4lS9eoicbmM9B2V6wP3H0ZS5h/3w4=', 'email': 'olsonkeith@example.net'}, {'username': 'dustinsmith', 'password': 'pbkdf2_sha256$1000000$rTQFdoFvhigF8myRBqUMGN$wT2cMeUZP+Nb5IYpmMsEbQ5tl5Q80kIh9Sb3LS+W/cc=', 'email': 'kimberlybailey@example.com'}, {'username': 'qtanner', 'password': 'pbkdf2_sha256$1000000$GU61rKMVAeN4cDrsC6bBNe$0Ipe+PPhUPCY0qTNNA+0JVjI5ovmQSX80dN2QgpyH5s=', 'email': 'wtaylor@example.org'}, {'username': 'jameshester', 'password': 'pbkdf2_sha256$1000000$ucVtIEiaoirXYjjgpw3kZa$suiiLetzZY3z0TxbjZQ5tJtpDAjPc5f6jpyFO0zhCl4=', 'email': 'amy98@example.org'}, {'username': 'jonestheresa', 'password': 'pbkdf2_sha256$1000000$XRPlpG8GdIIHJ3sQCPsZ1h$fkegfkX27AlHNnLcRNMfEYMOf388L1sWu0H0iha7va8=', 'email': 'mary86@example.org'}, {'username': 'iharrison', 'password': 'pbkdf2_sha256$1000000$s0ZANTDtBrR6ULUfGSpcTR$C5Rk1YR1nn/d1Tw7pHPPvMBc/+rtv/E8kWf3ToG+a8Q=', 'email': 'carolgutierrez@example.org'}, {'username': 'butlerderek', 'password': 'pbkdf2_sha256$1000000$EOhb7OeZh5OxtSmBw9FsHt$494b3fQH82mdyzaqt8HEULiEYbP+PrIZiMfUrmzBcbc=', 'email': 'sandrabarker@example.org'}, {'username': 'robertcampbell', 'password': 'pbkdf2_sha256$1000000$H6SNucj0BRIQBy9GjSAd8G$EomfyM5mXbGZEQ2CVGzDH/XUQk+1sO5fSPnGJTMu6Wg=', 'email': 'anthonyhays@example.net'}, '...(remaining elements truncated)...']