from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.template import RequestContext
from .forms import user_form


def home_view(request, *args, **kwargs):
    # template = loader.get_template("home.html")
    # return HttpResponse("<h1>test home page</h1>")
    return render(request, "home.html", {})


def form_view(request):
    form = user_form()

    if request.method == 'POST':
        print(request.POST)

    context = {'form': form}
    return render(request, 'display_name.html', context)
