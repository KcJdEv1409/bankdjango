from django.shortcuts import render
from custregpg.forms import CustRegstForm
from django.http import HttpResponse

# Create your views here.

def form_view(request):
    form = CustRegstForm()
    if request.method == 'POST':
        form = CustRegstForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form" : form}
    return render(request, "register.html", context)

def home(request):
    return HttpResponse("home page")