from django.shortcuts import render, redirect, HttpResponse
import random
from time import gmtime, strftime


def index(request):
    if 'gold_amt' and 'activity' not in request.session:
        request.session['gold_amt'] = 0
        request.session['activity'] = []
    return render(request, 'index.html')

def process_money(request):
    location = request.POST['location']
    date_time = strftime("%A, %B %d, %Y at %I:%M %p", gmtime())
    
    gold = {
        'farm':random.randint(10,20),
        'cave': random.randint(5,10),
        'house':random.randint(2,5),
        'casino':random.randint(-50,50),
    }
    
    if request.method == "POST":
        request.session['gold_amt'] += gold[location]
        if gold[location] < 0:
            message = f"You earned {gold[location]} gold from the {location} on {date_time}. You should stop gambling!"
        else:
            message = f"You earned {gold[location]} gold from the {location} on {date_time}. Nice!"

        request.session['activity'].append(message)
    else:
        request.session.flush()
    return redirect("/") 

def reset(request):
    request.session.flush()
    return redirect("/")