from django.shortcuts import render
from .models import Jobs

# Create your views here.
def home(request):
    job = Jobs.objects.all
    return render(request, 'jobs/index.html', {'jobs':job})
