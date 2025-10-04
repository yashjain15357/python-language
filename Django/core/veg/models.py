from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Recp(models.Model):
    user = models.ForeignKey(User , on_delete=models.SET_NULL,null=True, blank= True)  #When the referenced object (e.g., a User) is deleted, all related objects (e.g., Recp recipes) are also deleted automatically.

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