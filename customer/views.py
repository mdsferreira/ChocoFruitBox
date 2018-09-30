from django.shortcuts import render

def index(request):
    context = {'customer': "test"}
    return render(request, 'customer/index.html', context)