from django.shortcuts import render, get_object_or_404
from attendance_book.models import Attendance

# Create your views here.

def list(request):
    student_list = Attendance.objects.all()
    return render(request, 'attendance_book/index.html', {
        'student_list' : student_list,
        })

def profile(request, pk):
    student = get_object_or_404(Attendance, pk=pk)

    return render(request, 'attendance_book/detail.html', {
        'student' : student
        })