from django.shortcuts import render
from django.http import HttpResponse
from questions.models import Question
from answers.models import Answer

def index(request):

    questions = Question.objects.all()

    answers = Answer.objects.all()

    response = render(request, 'templates/home.html', { 'qs': questions, 'answers':answers })


    return response



def ask_questions(request):
    if request.method == 'GET':
        return render(request, 'templates/questions.html')

    elif request.method == 'POST' :
        quest_text =  (request.POST.get('question'))
        q = Question.objects.create(text=quest_text, downvotes=0)
        q.save()
        return HttpResponse('Question Saved!')

    else:
        return HttpResponse('404!')
