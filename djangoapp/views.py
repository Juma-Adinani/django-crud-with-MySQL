from django.http import HttpResponse
from django.shortcuts import redirect, render
from djangoapp.models import Students
from djangoapp.forms import StudentForm

# Create your views here.


def home(request):
    return redirect("/display")


def show_students(request):
    students = Students.objects.all()
    if students:
        return render(request, 'display.html', {'students': students})
    else:
        message = "No available student yet.."
        return render(request, 'no-students.html', {'message':message})


def add_students(request):
    if request.method == 'POST':
        student_form = StudentForm(request.POST, request.FILES)
        if student_form.is_valid():
            try:
                if student_form.save():
                    return redirect("/display")
                else:
                    return HttpResponse("<h4 style='color:red'>[ERROR]:   Failed to add a student...</h4>")
            except:
                pass
        else:
            return HttpResponse("<h4 style='color:red'>[ERROR]:   Form is invalid..</h4>")
    else:
        student_form = StudentForm()
    return render(request, 'insert.html', {'students_form': student_form})


def delete_students(request, id):
    student = Students.objects.get(id=id)
    student.delete()
    return redirect('/display')


def update_students(request, id):
    student = Students.objects.get(id=id)
    student_form = StudentForm(
        request.POST, request.FILES or None, instance=student)
    if student_form.is_valid():
        try:
            student_form.save()
            return redirect("/display")
        except:
            pass
    return render(request, 'update.html', {'student': student})
