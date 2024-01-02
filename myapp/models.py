from django.db import models


# Create your models here.

# Django ORM (object relational mapper)

class Course(models.Model):
    course_title = models.CharField(max_length=100)
    course_fees = models.IntegerField()

    def __str__(self):
        return self.course_title


class Student(models.Model):
    roll_no = models.IntegerField()
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    mobile_no = models.IntegerField()
    city = models.CharField(max_length=100)
    student_image = models.ImageField(upload_to='student_image', null=True, blank=True)

    def __str__(self):
        return self.name + "-" + str(self.roll_no)


class Teacher(models.Model):
    emp_id = models.IntegerField()
    name = models.CharField(max_length=100)
    mobile = models.IntegerField()
    salary = models.IntegerField()
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name + "-" + str(self.emp_id)


# ==============================================
gender_choice = (('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other'))  # dropdown
from django.core.validators import RegexValidator, MinLengthValidator


class employee(models.Model):
    emp_id = models.CharField(max_length=20, primary_key=True, default='ABCD')
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=6, choices=gender_choice)
    mobile = models.CharField(max_length=10, validators=[RegexValidator(regex='^[6-9\d{9}$',
                                                                        message='mobile is not valid')])  # MinLengthValidatofor min length nikalne ke liyer

    def __str__(self):
        return self.emp_id + " " + self.name

# ======================================================================================
