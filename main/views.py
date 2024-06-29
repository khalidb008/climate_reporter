from django.shortcuts import render, redirect, get_object_or_404
from .forms import climateform
from .models import climate
import logging

logger = logging.getLogger(__name__)

def index(request):
    climatedata = climate.objects.all()
    
    if request.method == 'POST':
        form = climateform(request.POST)
        if form.is_valid():
            climate_instance = form.save()
            logger.info("Data saved: %s", climate_instance)
            return redirect('climate_submit', climate_id=climate_instance.id)
        else:
            logger.error("Form errors: %s", form.errors)
    else:
        form = climateform()
    
    context = {
        'climatedata': climatedata,
        'form': form,
    }
    return render(request, 'index.html', context)

def climate_submit(request, climate_id=None):
    submitted_data = {}
    climatedata = climate.objects.all()

    if climate_id:
        climate_instance = get_object_or_404(climate, id=climate_id)
        submitted_data = {
            'city': climate_instance.city,
            'temperature': climate_instance.temperature,
            'flood': climate_instance.flood,
            'wind_speed': climate_instance.wind_speed,
            'carbon_emission': climate_instance.carbon_emission,
            'drought': climate_instance.drought,
            'rainfall': climate_instance.rainfall,
        }

    context = {
        'submitted_data': submitted_data,
        'climatedata': climatedata,
    }

    return render(request, 'climate_submit.html', context)


from django.shortcuts import render

def base_view(request):
    climatedata = climate.objects.all()  # Query to retrieve all Climate objects
    
    context = {
        'climatedata': climatedata  # Pass climate data to the template context
    }
    
    return render(request, 'base.html', context)