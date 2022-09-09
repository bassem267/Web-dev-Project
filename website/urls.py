from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.projects, name = 'projects'),
    path('homepage', views.homepage, name = 'homepage'),
    path('studentlist', views.liststudents, name='liststudent'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('update/updaterecord/<int:id>',
         views.updaterecord, name='updaterecord'), 
    path('addstudent/', views.addstudent, name='addstudent'),
    path('addstudent/addrec/', views.addrec, name='addrec'),
    path('addCourses/', views.addCourses, name='addCourses'),
    path('addCourses/addrecord/', views.addrecord, name='addrecord'),
    path('searchStudent/', views.searchStudent, name='searchStudent'),
    path('searchStudent/registration/<int:id>',
         views.registration, name='registration'),
    path('searchStudent/registration/registration_update/<int:id>',
         views.registration_update, name='registration_update'),
    path('listcourses', views.listcourses, name='listcourses'),
    path('delete1/<int:id>', views.delete1, name='delete1'),
    path('update1/<int:id>', views.update1, name='update1'),
    path('update1/updaterecord1/<int:id>',
         views.updaterecord1, name='updaterecord1'),
]

