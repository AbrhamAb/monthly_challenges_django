from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
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
def monthly_challenge_by_number(request,month):
    months=list(challenges.keys())
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge",args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request,month):
    try:
        challenge_text=challenges[month]
        response_data = f"<h1>{month.capitalize()}</h1><p>{challenge_text}</p>"
    except:
        return HttpResponseNotFound("<h1> Invalid month </h1>")
    return HttpResponse(response_data)