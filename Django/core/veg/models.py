from django.db import models

# Create your models here.
class Recp(models.Model):
    recp_name = models.CharField(100 , null=False)
    recp_decp= models.TextField()
    recp_img = models.ImageField(upload_to="recp")
