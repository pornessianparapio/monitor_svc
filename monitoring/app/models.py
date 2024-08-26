from django.db import models

class Admin(models.Model):
    admin_name = models.CharField(max_length=100)
    admin_email = models.EmailField(unique=True)
    admin_password = models.CharField(max_length=128)  # Increased length for hashed password

    def __str__(self):
        return self.admin_email

    class Meta:
        db_table = "Admin"
