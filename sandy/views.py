from django.shortcuts import render
from .models import Home, Service, Portfolio, Education

# Create your views here.
def index(request):
    home = Home.objects.latest('updated')
    service = Service.objects.latest('updated')
    portfolio = Portfolio.objects.latest('updated')
    education = Education.objects.latest('updated')
    
    context = { 'home': home, 'service': service, 'portfolio': portfolio, 'education': education }

    return render(request, 'index.html', context)