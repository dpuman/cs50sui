from django.shortcuts import render
from django.http import Http404, HttpResponse

# Create your views here.


def index(request):
    return render(request, 'singleapp/index.html')


texts = ['text-1', 'text-2', 'text-3']


def section(request, num):
    if(1 <= num <= 3):
        return HttpResponse(texts[num-1])
    else:
        raise Http404('No such Option')