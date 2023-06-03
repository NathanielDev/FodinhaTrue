from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import MyForm
from django.template import RequestContext


def sample_view(request):
    template = loader.get_template("home.html")
    return HttpResponse(template.render())


def my_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            # Process the form data as needed
            # Redirect or render a response
    else:
        form = MyForm()
    return render(RequestContext(request), 'home.html', {'form': form})
