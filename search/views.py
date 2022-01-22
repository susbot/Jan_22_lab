from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

projectslist = [
    {
        'id':'1',
        'title': 'woof Website',
        'description': 'random one'
    },
    {
        'id':'2',
        'title': 'quack website',
        'description': 'random two'
    },
    {
        'id': '3',
        'title': 'meow website',
        'description':'random three'
    },
]

def projects(request):
    page = 'projects'
    number = 10
    context = {'page':page, 'number': number, 'projects': projectslist}
    return render(request, 'content/projects.html', context)

def project(request, pk):
    projectObj = None
    for i in projectslist:
        if i['id'] == pk:
            projectObj = i
    return render(request, 'content/single.html', {'project': projectObj})
