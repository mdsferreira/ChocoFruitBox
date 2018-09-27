from django.shortcuts import render

# def register(request):
#     return render(request, 'success.html', {})

def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'customer': "test"}
    return render(request, 'customer/index.html', context)