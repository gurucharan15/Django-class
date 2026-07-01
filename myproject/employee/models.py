from django.db import models

# Slide 12 & 23: Django Models and ORM Demo
class Employee(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=100, verbose_name="Full Name")
    email = models.EmailField(unique=True, verbose_name="Email Address")
    department = models.CharField(max_length=50, default="General", verbose_name="Department")
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=50000.00, verbose_name="Salary")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.email})"

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Employee"
        verbose_name_plural = "Employees"
