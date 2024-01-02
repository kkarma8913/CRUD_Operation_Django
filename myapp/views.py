from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import StudentForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from myapp.models import *
from django.contrib.auth.decorators import login_required

from .models import Teacher, Student


# =====================================================================================
# Sign Up

def sign_up(request):
    if request.method == 'POST':
        myform = UserCreationForm(request.POST)
        if myform.is_valid():
            myform.save()
        return redirect('home')
    else:
        myform = UserCreationForm()
        return render(request, 'sign_up.html', {'myform': myform})


# ======================================================================================

def log_in(request):
    if request.method == 'POST':
        myform = AuthenticationForm(data=request.POST)
        if myform.is_valid():
            uname = myform.cleaned_data['username']
            upass = myform.cleaned_data['password']

            user = authenticate(username=uname, password=upass)

            if user:
                login(request, user)

                request.session['user_name'] = uname

            return redirect('home')

    else:
        myform = AuthenticationForm()
        return render(request, 'log_in.html', {'myform': myform})


# ========================================================================================

def log_out(request):
    logout(request)
    return redirect('log_in')


# ====================================================================================


# Create your views here.

def home(request):
    return render(request, 'home.html')


def index(request):
    return HttpResponse('<h1>this is index page</h1>')


def page1(request):
    return render(request, 'page1.html')


def welcome(request):
    language = ['JAVA', 'Csharp', 'Python', 'Ruby', 'HTML', 'CSS', 'React', 'Angular', 'Mongodb', 'SQL']
    student_name = ['avinash', 'ritesh', 'pratik', 'ankit', 'priyanka']

    return render(request, 'welcome_codebetter.html', {'data': language, 'student_data': student_name})


# render(request,HTML file name, data)


# ==============================================================================

# Read Data
# def show_students(request):
#     if request.method == 'POST':
#         course_id = request.POST['course_id'] # 1,2,3,4....., All
#         if course_id == 'All':
#             course_obj = None
#         else:
#              course_obj = Course.objects.get(id = course_id)

#         course_data = Course.objects.all()
#         if course_obj != None :
#             data = Student.objects.filter(course = course_obj)
#         else:
#             data = Student.objects.all()
#         return render(request,'student_detail.html',{'student_data':data,'course_data':course_data})

#     else:
#         course_data = Course.objects.all()
#         data = Student.objects.all()
#         return render(request,'student_detail.html',{'student_data':data,'course_data':course_data})

# =============================================================================
# Read Data
def show_students(request):
    course_data = Course.objects.all()
    data = Student.objects.all()

    city = []

    all_data = Student.objects.all()
    for i in all_data:
        city.append(i.city)

    city_data = list(set(city))

    return render(request, 'student_detail.html',
                  {'student_data': data, 'course_data': course_data, 'city_data': city_data})


# ===============================================================================

def student_filter(request):
    course_id = request.POST['course_id']  # 1,2,3,4....., All
    if course_id == 'All':
        course_obj = None
    else:
        course_obj = Course.objects.get(id=course_id)

    course_data = Course.objects.all()
    if course_obj != None:
        data = Student.objects.filter(course=course_obj)
    else:
        data = Student.objects.all()

    city = []

    all_data = Student.objects.all()
    for i in all_data:
        city.append(i.city)

    city_data = list(set(city))

    return render(request, 'student_detail.html',
                  {'student_data': data, 'course_data': course_data, 'city_data': city_data})


# =================================================================================

def student_city(request):
    city = request.POST['city']  # 1,2,3,4....., All

    course_data = Course.objects.all()
    if city != 'All':
        data = Student.objects.filter(city=city)
    else:
        data = Student.objects.all()

    city = []

    all_data = Student.objects.all()
    for i in all_data:
        city.append(i.city)

    city_data = list(set(city))

    return render(request, 'student_detail.html',
                  {'student_data': data, 'course_data': course_data, 'city_data': city_data})

@login_required

def show_teachers(request):
    data = Teacher.objects.all()
    return render(request, 'show_teacher.html', {'teacher_data': data})


# ================================================================================
# Create Data
# def add_student(request):
#     if request.method == 'POST':
#         roll_no = request.POST['roll_no']
#         name= request.POST['name']
#         course = request.POST['course']
#         mobile_no = request.POST['mobile_no']
#         city = request.POST['city']

#         student_obj = Student(name=name,roll_no=roll_no,course=course,mobile_no=mobile_no,city=city)
#         student_obj.save()
#         msg = 'Student added'
#         return render(request,'student_add.html',{'msg':msg})
#     else:
#         return render(request,'student_add.html')


# =====================================================================================
# Update Data
# def upd_student(request,id):
#     if request.method=='POST':
#         stu_id  = Student.objects.get(id = id)
#         roll_no = request.POST['roll_no']
#         name= request.POST['name']
#         course = request.POST['course']
#         mobile_no = request.POST['mobile_no']
#         city = request.POST['city']

#         student_obj = Student(id=stu_id.id,name=name,roll_no=roll_no,course=course,mobile_no=mobile_no,city=city)
#         student_obj.save()
#         msg = 'Student update'
#         return render(request,'update_student.html',{'msg':msg})

#     else:
#         student_data  = Student.objects.get(id = id)
#         return render(request,'update_student.html',{'student_data':student_data})
# ============================================================================================

# Delete data
def del_student(request, id):
    student_data = Student.objects.get(id=id)
    student_data.delete()
    return redirect('show_student')


# ========================================================================


# def add_student(request):
#    if request.method == 'POST':
#        myform = StudentForm(request.POST)
#        if myform.is_valid():
#            myform.save()
#        return redirect('show_student')
#    else:
#        myform = StudentForm()
#        heading = 'Add Student'
#        return render(request,'add_stu.html',{'myform':myform,'heading':heading})

# ================================================================================

def upd_student(request, id):
    if request.method == 'POST':
        obj = Student.objects.get(id=id)
        myform = StudentForm(request.POST, request.FILES, instance=obj)
        if myform.is_valid():
            myform.save()
        return redirect('show_student')
    else:
        obj = Student.objects.get(id=id)
        myform = StudentForm(instance=obj)
        heading = 'Update Student'
        return render(request, 'add_stu.html', {'myform': myform, 'heading': heading})


# ====================================================================================

# Function based view
# class based view

# ====================================================================================

from django.views import View
class AddStudent(View):
    def get(self, request):
        myform = StudentForm()
        heading = 'Add Student'
        return render(request, 'add_stu.html', {'myform': myform, 'heading': heading})

    def post(self, request):
        myform = StudentForm(request.POST, request.FILES)
        if myform.is_valid():
            myform.save()
        return redirect('show_student')


# ==================================================================================

def filter_show(request):
    data = Student.objects.filter(course__icontains='BB')
    return render(request, 'student_detail.html', {'student_data': data})










