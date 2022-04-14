from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request, 'week1/index.html')

def about_view(request):
    return render(request, 'week1/about.html')

def welcome_view(request):
    return render(request, 'week1/welcome.html', context={
        'weeks' : 5,
        'course' : 'Flask',
        'group' : 'A 0101'
    })

def student_view(request, student_id):
    students = {
        1: "Смирнов Хольгер Филиппович",
        2: "Демидович Налина Кирилловна",
        3: "Рыбакова Хитер Валерьевна",
        4: "Жуков Орион Святославович",
    }
    student = students[student_id]
    return render(request, 'week1/student.html', context={
        'student': student
    })