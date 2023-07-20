from django.shortcuts import render
from .models import Sostav


def index(request):
    player = Sostav.objects.all()
    return render(request, 'sostav/index.html', {'player': player})
