from django.shortcuts import render,redirect
from .models import *
from .forms import *
# Create your views here.
def home(request):
    depart_form = Department_form()
    student_form = Student_form()
    return render(request,'app1/home.html',{'depart_form':depart_form,'stu_form':student_form})

def depart_detail(request):
    if request.method == 'POST':
        department = request.POST['Department_name']
        department_descripsion = request.POST['Deparment_descrip']

        depart = Departments.objects.filter(Department_name = department)
        if depart:
            depart_form = Department_form()
            return render(request, 'app1/home.html',{'depart_form':depart_form})
        else:
            depart_form = Department_form()
            student_form = Student_form()
            Departments.objects.create(Department_name= department, Deparment_descrip= department_descripsion)
            return render(request, 'app1/stu.html',{'depart_form':depart_form,'stu_form':student_form})
        

def stu_details(request):
    student_form = Student_form()
    if request.method == 'POST':
        name = request.POST['Name']
        email = request.POST['Email']
        contact = request.POST['Contact']
        department = request.POST['Department']

        stu = Students.objects.filter(Email = email)
        if stu:
            message = 'all-ready department alloted'
            student_form = Student_form()
            return render(request, 'app1/home.html',{'msg':message,'stu_form':student_form})
        else:
            message = "department alloted sucessfully"
            stu_data = Departments.objects.get(id = department)
            depart_form = Department_form()
            student_form = Student_form()
            Students.objects.create(Name=name,Email=email,Contact=contact,Department=stu_data)
            return render(request, 'app1/home.html',{'msg':message,'depart_form':depart_form})


