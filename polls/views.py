from django.http import HttpResponse
from .models import questions
from django.shortcuts import render, get_object_or_404,redirect

import random 


def index(request):
    return HttpResponse("hello ")


def question_view(request, question_id):
    question = get_object_or_404(questions, id=question_id)

    if request.method == 'POST':
        selected_option = request.POST.get('option')
       

        if selected_option == question.option1:
            question.option1_count += 1
        elif selected_option == question.option2:
            question.option2_count += 1
        elif selected_option == question.option3:
            question.option3_count += 1

        question.save()
        return redirect('project')

    context = {
        'question': question
    }
    return render(request, 'project/question_detail.html', {'question': question})


def project(request):
    details = questions.objects.all()
    context = {
        "details" : details
    }
    return render(request,"project/project.html",context)



def results(request):
    details = questions.objects.all()
    context = {
        "details" :details
    }
    return render(request,"project/results.html",context)