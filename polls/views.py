from django.shortcuts import render

from django.http import (HttpResponse, Http404)
from .models import Question
from django.views import generic

from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateView

from django.utils import timezone


class IndexView(generic.ListView):
  template_name = 'index.html'
  context_object_name = 'questions'
  
  def get_queryset(self):
    return Question.objects.all()
  
  

# def index(request):
#   questions = Question.objects.all()
#   context = {
#     'questions':questions
#   }
#   return render(request,"index.html",context)

class DetailView(generic.DetailView):
  model = Question
  template_name='details.html'
  

# def details(request,question_id):
  
#   # try:
#   #   question = Question.objects.get(id=question_id)
#   # except:
#   #   raise Http404("Cette question n'existe pas")
  
#   question = get_object_or_404(Question, pk=question_id)
#   context = {
#     "question": question
#   }
  
  # return render(request,"details.html",context)

# Create your views here.

# demande : GET, POST, PUT, DELETE


def getQuestion(request):
  questions = Question.objects.all()
  return render(request,'index.html',{
    "questions":questions
    })
  
  
def create_question(request):
  question = Question.objects.create(
    question_text=request.GET.get('question'),
    pub_date=timezone.now())
  questions = Question.objects.all()
  return render(request,'index.html',{"questions":questions})


# def addQuestion(request):   
#   if request.POST:
#     question = Question.objects.create(
#     question_text=request.POST.get('question'),
#     pub_date=timezone.now())
#     return render(request,'details.html',{"question":question})
#   else:
#      return render(request,'addQuestion.html')
  
  
class QuestionView(TemplateView):
  def get(self,request):
    return render(request,'addQuestion.html')
  
  def post( self, request):
    question = Question.objects.create(
    question_text=request.POST.get('question'),
    pub_date=timezone.now())
    return render(request,'details.html',{"question":question})
    
  