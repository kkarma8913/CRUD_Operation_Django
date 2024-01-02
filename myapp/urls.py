from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.home, name='home'),
    path('index/',views.index),
    path('page1/',views.page1),
    path('wel',views.welcome),
    path('show_student',views.show_students,name='show_student'),
    path('show_teachers',views.show_teachers, name='show_teachers'),
    # path('add_student',views.add_student, name='add_student'),
    path('upd_student/<id>',views.upd_student, name='student_update'),
    path('student_del/<id>',views.del_student, name='student_del'),

    # class based url

    path('add_student',views.AddStudent.as_view(), name='add_student'),
    path('filter',views.filter_show),

    # authentication
    path('sign_up',views.sign_up, name = 'sign_up'),
    path('log_in',views.log_in, name='log_in'),
    path('log_out',views.log_out, name='log_out'),

    path('student_filter', views.student_filter,name ='student_filter'),
    path('student_city',views.student_city,name = 'student_city')
]