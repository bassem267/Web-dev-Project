from django.shortcuts import render
from django.forms import modelform_factory
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Student, Course
from django.template.loader import render_to_string
from django.http import JsonResponse


# Create your views here.

def projects(request):
    template = loader.get_template('pages/projectsHomepage.html')
    return HttpResponse(template.render({}, request))

def homepage(request):
    template = loader.get_template('pages/HomePage.html')
    return HttpResponse(template.render({}, request))

def addstudent(request):
    courses = Course.objects.all().values()
    template = loader.get_template('pages/addStudent.html')
    context ={
        'courses': courses,
    }
    return HttpResponse(template.render(context, request))

def addrec(request):
    name = request.POST['studentName']
    sid = request.POST['id']
    date = request.POST['date']
    uni = request.POST['uni']
    dept = request.POST['dept']
    gender = request.POST['gender']
    stat = request.POST['gridRadios1']
    course1 = request.POST['course1']
    course2 = request.POST['course2']
    course3 = request.POST['course3']
    student = Student(studentName=name, studentID=sid, dateOfBirth= date,
                      university=uni, studentDepartment=dept, gender=gender, status=stat,
                      course1=course1, course2=course2, course3=course3)
    student.save()

    return HttpResponseRedirect(reverse('addstudent'))

def liststudents(request):
    students = Student.objects.all().values()
    template = loader.get_template('pages/active-inactive students.html')
    context = {
        'students': students,
    }
    return HttpResponse(template.render(context, request))

def delete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return HttpResponseRedirect(reverse('liststudent'))

def update(request, id):
    student = Student.objects.get(id=id)
    courses = Course.objects.all().values()
    template = loader.get_template('pages/editStudent.html')
    context = {
        'student': student,
        'courses': courses,
    }
    return HttpResponse(template.render(context, request))

def updaterecord(request, id):
    name = request.POST['studentName']
    sid = request.POST['id']
    date = request.POST['date']
    uni = request.POST['uni']
    dept = request.POST['dept']
    gender = request.POST['gender']
    stat = request.POST['gridRadios1']
    course1 = request.POST['course1']
    course2 = request.POST['course2']
    course3 = request.POST['course3']
    student = Student.objects.get(id=id)
    student.studentName = name
    student.studentID = sid
    student.dateOfBirth = date
    student.university = uni
    student.studentDepartment = dept
    student.gender = gender
    student.status = stat
    student.course1 = course1
    student.course2 = course2
    student.course3 = course3
    student.save()
    return HttpResponseRedirect(reverse('liststudent'))

def addCourses(request):
    template = loader.get_template('pages/addCourses.html')
    return HttpResponse(template.render({}, request))

def addrecord(request):
    name = request.POST['courseName']
    cid = request.POST['courseID']
    dept = request.POST['department']
    hours = request.POST['hours']
    day = request.POST['day']
    hall = request.POST['hallNumber']
    
    course = Course(courseName= name, courseID=cid, department=dept,
                    numberOfHours= hours, lectureDay= day, hallNumber = hall)
    course.save()
    
    return HttpResponseRedirect(reverse('listcourses'))

def searchStudent(request):
    ctx = {}
    url_parameter = request.GET.get("q")
    
    if url_parameter:
        students = Student.objects.filter(
            studentName__istartswith=url_parameter, status=True)
    else:
        students = Student.objects.all()
    
    ctx["students"] =  students
    does_req_accept_json = request.accepts("application/json")
    is_ajax_request = request.headers.get(
        "x-requested-with") == "XMLHttpRequest" and does_req_accept_json

    if is_ajax_request:
        
        html = render_to_string(
            template_name="pages/listing.html", context={"students": students}
        )
        data_dict = {"html_from_view": html}
        return JsonResponse(data=data_dict, safe=False)
    
    return render(request, "pages/SearchStudent.html", context=ctx)

def registration(request, id):
    student = Student.objects.get(id=id)
    courses = Course.objects.all().values()
    template = loader.get_template('pages/course registration.html')
    context = {
        'student': student,
        'courses': courses,
    }
    return HttpResponse(template.render(context, request))

def registration_update(request, id):
    course1 = request.POST['course1']
    course2 = request.POST['course2']
    course3 = request.POST['course3']
    student = Student.objects.get(id=id)
    student.course1 = course1
    student.course2 = course2
    student.course3 = course3
    student.save()
    return HttpResponseRedirect(reverse('searchStudent'))

def listcourses(request):
    courses = Course.objects.all().values()
    template = loader.get_template('pages/courselist.html')
    context = {
        'courses': courses,
    }
    return HttpResponse(template.render(context, request))

def delete1(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    return HttpResponseRedirect(reverse('listcourses'))

def update1(request, id):
    course = Course.objects.get(id=id)
    template = loader.get_template('pages/editCourse.html')
    context = {
        'course': course,
    }
    return HttpResponse(template.render(context, request))

def updaterecord1(request, id):
    name = request.POST['courseName']
    cid = request.POST['courseID']
    dept = request.POST['department']
    hour = request.POST['hours']
    day = request.POST['day']
    hall = request.POST['hallNumber']
    course = Course.objects.get(id=id)
    course.courseName = name
    course.courseID = cid
    course.department = dept
    course.numberOfHours = hour
    course.lectureDay = day
    course.hallNumber = hall
    course.save()
    return HttpResponseRedirect(reverse('listcourses'))
