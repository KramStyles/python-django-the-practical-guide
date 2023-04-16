from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import reverse, redirect

# Create your views here.

daily_challenges = {
        "monday": "Make weekly plans",
        "tuesday": "Reflect on previous day",
        "wednesday": "Read 5 books",
        "thursday": "Visit your friends",
        "friday": "Play games",
        "saturday": "Build your empire",
        "sunday": "Think and worry less",
    }

def challenge_home(request):
    iterated_list = ""

    for day in daily_challenges:
        iterated_list += f"<li><a href='{reverse('weekly-activities', args=[day])}'>{day.title()}</a></li>"
    response_data = f"""
        <ul>
            {iterated_list}
        </ul>
    """
    return HttpResponse(response_data)

def index(request, day):
    # result = daily_challenges.get(month.lower()) or "Month not listed"
    result = daily_challenges.get(day.lower())

    if not result:
        return HttpResponseNotFound("<h2>Day not supported!</h2>")
    return HttpResponse(f"<h2>{result}</h2>")

def daily_challenge_by_number(request, day):
    # Here we will redirect to the appropriate day
    week = list(daily_challenges.keys())
    try:
        day = week[day-1]
        return redirect("weekly-activities", day=day)
    except IndexError as err:
        print(err)
        return HttpResponseNotFound(f"<h2>{err}</h2>")
