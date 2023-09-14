from django.db import models


# Create your models here.

# class Department(models.Model):
#     DEPARTMENT_CHOICES = [
#         ('Computer Science', 'Computer Science'),
#         ('Commerce', 'Commerce'),
#         ('Humanities', 'Humanities'),
#         ('Bio Maths', 'Bio Maths'),
#         ('VHSE', 'VHSE'),
#     ]
#     name = models.CharField(max_length=100,choices=DEPARTMENT_CHOICES)
#
#     def __str__(self):
#         return self.name


# Model for Course
# class Course(models.Model):
#     name = models.CharField(max_length=100)
#     department = models.ForeignKey(Department, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.name


class Student(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    # DEPARTMENT_CHOICES = [
    #     ('Computer Science', 'Computer Science'),
    #     ('Commerce', 'Commerce'),
    #     ('Humanities', 'Humanities'),
    #     ('Bio Maths', 'Bio Maths'),
    #     ('VHSE', 'VHSE'),
    # ]

    PURPOSE_CHOICES = [
        ('Enquiry', 'Enquiry'),
        ('Place Order', 'Place Order'),
        ('Return', 'Return'),
        ('Reporting', 'Reporting'),
        ('Placements', 'Placements'),
    ]

    # MATERIALS_CHOICES = [
    #     ('Note', 'Note'),
    #     ('pen', 'pen'),
    #     ('paper', 'paper'),
    # ]

    # COURSE_CHOICES = [
    #     "Computer Science:"('Notebook', 'Notebook'),
    #     ('pen', 'pen'),
    #     ('paper', 'paper'),
    # ]

    name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)
    address = models.TextField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    age = models.IntegerField()
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    department = models.CharField(max_length=50)
    # department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    purpose = models.CharField(max_length=50, choices=PURPOSE_CHOICES)
    course=models.CharField(max_length=50)
    # course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    note = models.BooleanField(default=False)
    pen = models.BooleanField(default=False)
    paper = models.BooleanField(default=False)
    # material=models.BooleanField(default=False)

    def __str__(self):
        return self.name
