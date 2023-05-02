from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import reverse, redirect, render
from django.views import View
from django.views.generic import TemplateView, DetailView

from challenges.forms import ReviewForm, ReviewModelForm
from challenges.models import Review

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
        context = {"title": "page not found", "reason": str(err)}
        # raise Http404()
        return render(request, "challenges/404.html", context)


def reviews(request):
    context = {"title": "reviews"}
    if request.method == "POST":
        form = ReviewModelForm(request.POST)
        if form.is_valid():
            # data = form.cleaned_data
            # Review.objects.create(
            #     username=data.get("username"),
            #     ratings=data.get("ratings"),
            #     review=data.get("review_text"),
            # )
            form.save()
            context.update(
                {"status": "success", "message": "Details saved successfully"}
            )
            form = ReviewModelForm()
        else:
            context.update(
                {
                    "status": "error",
                    "message": "Error(s) occurred. Find information below!",
                }
            )
    else:
        form = ReviewModelForm()
    context["form"] = form
    return render(request, "challenges/reviews/reviews.html", context)


class Reviews(View):
    def __init__(self):
        self.context = {"title": "reviews with class"}

    def get(self, request):
        self.context["form"] = ReviewModelForm()
        return render(request, "challenges/reviews/reviews.html", self.context)

    def post(self, request):
        form = ReviewModelForm(request.POST)
        if form.is_valid():
            form.save()
            self.context.update(
                {"status": "success", "message": "Details saved successfully"}
            )
            form = ReviewModelForm()
        else:
            self.context.update(
                {
                    "status": "error",
                    "message": "Error(s) occurred. Find information below!",
                }
            )
        return render(request, "challenges/reviews/reviews.html", self.context)


class BaseView:
    def __init__(self):
        self.context = {}

    def get_context_data(self, **kwargs):
        self.context = super().get_context_data(**kwargs)
        return self.context


class ReviewListTemplateView(BaseView, TemplateView):
    template_name = "challenges/reviews/reviews-list.html"

    def get_context_data(self, **kwargs):
        self.context["title"] = "Review List"
        self.context["reviews"] = Review.objects.all()
        return self.context


class ReviewDetailView(BaseView, DetailView):
    model = Review
    template_name = "challenges/reviews/reviews-detail.html"

    def get_context_data(self, **kwargs):
        self.context = super().get_context_data(**kwargs)
        self.context["title"] = f"Ratings by {self.object.username.title()}"
        return self.context


def not_found_page(request):
    # Todo: Ensure you fix this up for valid 404 page so when we call raise http404, this shows
    context = {
        "title": "page not found",
        "reason": "We can't find what you are searching for",
    }
    return render(request, "challenges/404.html", context)
