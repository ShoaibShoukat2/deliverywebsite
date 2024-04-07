from django.db import models

# Create your models here.



class Signup(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    remember_me = models.BooleanField(default=False)  # Add this line

    def __str__(self):
        return self.name





