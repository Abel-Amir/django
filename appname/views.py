from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from appname.models import Comment


def aizirek_1 (request):
    return HttpResponse("Создал папку, создал виртуальную среду. Создал проект blog и создал приложение appname и в приложении написал urls. Прописал 3 функции в views и 3 ссылки")
def aizirek_2 (request):
    return HttpResponse("В ссылках нужно указывать пути")
def aizirek_3 (request):
    return HttpResponse("Сегоднняшний день был очень продуктивным. Утром проснулся и попил лекарства, после поехал на работу. После работы поехал на учебу, после учебы пошел покушать, после еды поехал на работу и забрал униформу. После того как забрал униформу поехал домой и оставил вещи дома, потом взял ноутбук и поехал в гиктек для того что бы разобраться с проблемами и сделать дз.")
def comment_show (request):
    comments = Comment.objects.all()
    context = {"comments": comments}
    return render(request, "aizirek_4.html", context)