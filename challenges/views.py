from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import reverse, redirect, render

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
    context = {"title": "welcome"}

    for day in daily_challenges:
        iterated_list += f"""<li class='list-group-item d-grid'>
            <a href='{reverse('weekly-activities', args=[day])}'
            class='p-1'>{day.title()}</a>
            </li>"""
    response_data = f"""
        <ul class='list-group'>
            {iterated_list}
        </ul>
    """
    context["data"] = response_data
    return render(request, "challenges/home.html", context=context)


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
        day = week[day - 1]
        return redirect("weekly-activities", day=day)
    except IndexError as err:
        context = {
            'title': "page not found",
            "reason": str(err)
        }
        # raise Http404()
        return render(request, "challenges/404.html", context)
