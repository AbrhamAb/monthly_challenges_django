from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def monthly_challenge(request,month):
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
    challenge_text=challenges.get(month,"")
    return HttpResponse(challenge_text)