from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string 
# Create your views here.
challenges={
        "january":"Read 5 chapters of a book.",
        "february":"Walk for at least 20 minutes every day.",
        "march":"Learn Django for 20 minutes daily.",
        "april":"Practice meditation for 10 minutes.",
        "may":"Write a journal entry every night.",
        "june":"Drink 8 glasses of water daily.",
        "july":"Exercise for 30 minutes.",
        "august":"Cook a new recipe each week.",
        "september":"Read a technical article daily.",
        "october":"Take a 15-minute walk after lunch.",
        "november":"Practice gratitude journaling.",
        "december":"Reflect on the year's achievements."
    }

def index(request):
    list_items=""
    months=list(challenges.keys())

    for month in months:
        month_path=reverse("month-challenge",args=[month])
        list_items+=f"<li><a href='{month_path}'>{month.capitalize()}</a></li>"
    
    response_data=f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def monthly_challenge_by_number(request,month):
    months=list(challenges.keys())

    if month>len(months):
        return HttpResponseNotFound("<h1> Invalid month </h1>")
    else:
        redirect_month = months[month - 1] 
        redirect_path = reverse("month-challenge",args=[redirect_month])
        return HttpResponseRedirect(redirect_path)

def monthly_challenge(request,month):
    try:
        challenge_text=challenges[month]
        response_data = render_to_string("challenges/challenge.html")
    except:
        return HttpResponseNotFound("<h1> Invalid month </h1>")
    return HttpResponse(response_data)