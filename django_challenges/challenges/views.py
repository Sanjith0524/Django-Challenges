from django.shortcuts import render
from django.http import HttpResponseRedirect
from  django.urls import reverse
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
    'november' : None ,
    'december' : 'Eat no meat for the entire month '
}

def index(request):
    months = list(monthly_chalenges.keys())
    return render(request,'challenges/index.html',{'month':months})


def monthly_numbers (request,month):
    months = list(monthly_chalenges.keys())
    forward_month = months[month-1]
    redirect_path = reverse('month-challenge',args=[forward_month])
    return HttpResponseRedirect(redirect_path)
def monthly_challenges(request,month):
    try:
        challenge_text = monthly_chalenges[month]
        return render(request,"challenges/challenge.html",{'text':challenge_text,'months':month})
    except:
        return render(request,'404.html')
