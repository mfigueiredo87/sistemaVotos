from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
#query database query data
from .models import Question, Choice

#Get questions and display them
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

#shor specific question and choices
def detail(request, question_id):
    try:
     question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Esta Questão Não Existe!")
    return render(request, 'polls/detail.html', { 'question': question})

#metodo para mostrar resultados da questao
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question })

#metodo para votar
def vote(request, question_id):
    # print(request.POST['choice'])
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        #Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "Não selecionou a resposta.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        #retornar sempre uma HttpResponseRedirect depois de uma accao de sucesso com dado POST.
        # Isto provem de dados postados no inicio se o utilizador clica no botao voltar
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))