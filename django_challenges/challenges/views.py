from django.shortcuts import render
from django.http import HttpResponse , HttpResponseNotFound ,HttpResponseRedirect
from  django.urls import reverse
def index(request):
    list_items = ''
    months = list(monthly_chalenges.keys())

monthly_chalenges = {
    'january' : 'Eat no meat for the entire month ',
    'february' : "Exercise for atleast 1 hour ",
    'march' :  'Avoid junk' ,
    'april' : 'Do Cardio' ,
    'may' : 'Practice Django' ,
    'june' : 'Practice Java' ,
    'july' : 'Eat no meat for the entire month ' ,
    'august' : "Exercise for atleast 1 hour " ,
    'september' : 'Avoid junk' ,
    'october' : 'Practice Django' ,
    'november' : 'Practice Java' ,
    'december' : 'Eat no meat for the entire month '
}
def monthly_numbers (request,month):
    months = list(monthly_chalenges.keys())
    forward_month = months[month-1]
    redirect_path = reverse('month-challenge',args=[forward_month])
    return HttpResponseRedirect('/challenges/' + forward_month)
def monthly_challenges(request,month):
    try:
        challenge_text = monthly_chalenges[month]
        response_data = f'<h1>{challenge_text}</h1>'
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound('Error 404')
