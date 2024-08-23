from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Admin(models.Model):
    admin_name = models.CharField(max_length=100)
    admin_email = models.EmailField(unique=True)
    admin_password = models.CharField(max_length=32)

    def __str__(self):
        return f'{self.admin_email} {self.admin_password}'

    class Meta:
        db_table = "Admin"