from django.shortcuts import render

from todolist.models import Todolist

# Create your views here.
def index (request):
    todolist=Todolist.objects.order_by('id')
    content={'todolist':todolist}
    return render(request,'index.html',content)