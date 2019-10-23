from django.shortcuts import render


def index(request):
    context = dict(question=True)
    return render(request, 'dashboard/index.html', context)
