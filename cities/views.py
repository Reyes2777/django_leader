from django.shortcuts import render, redirect
from .models import Region, City
from .forms import RegionForm, CityForm
from .cities_controller import CitiesController


def index(request):
    """
    View that invoke principal page from templates, and use's methods of CitiesController, and Models

    """
    cities_controller = CitiesController()
    regions = cities_controller.prepare_dict()
    cities = cities_controller.get_cities_from_db()
    print('<<<<<<<<<<<<<<', regions, cities)
    return render(request, 'index.html', {'regions': regions, 'cities': cities})


def new_region(request):
    """
    View that invoke form for create new regions

    """
    form = RegionForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request, 'regions-form.html', {'form': form})


def new_city(request):
    """
    View that invoke form for create new citys

    """
    form = CityForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request, 'cities-form.html', {'form': form})


def update_region(request, id):
    """
    View that invoke form for update region

    """
    region = Region.objects.get(id=id)
    form = RegionForm(request.POST or None, instance=region)

    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request, 'regions-form.html', {'form': form, 'region': region})


def update_city(request, id):
    """
       View that invoke form for update city

    """
    city = City.objects.get(id=id)
    form = CityForm(request.POST or None, instance=city)

    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request, 'cities-form.html', {'form': form, 'city': city})


def delete_region(request, id):
    """
       View that invoke form for delete region

    """
    region = Region.objects.get(id=id)
    if request.method == 'POST':
        region.delete()
        return redirect('index')

    return render(request, 'region-delete.html', {'region': region})


def delete_city(request, id):
    """
       View that invoke form for delete city

    """
    city = City.objects.get(id=id)
    if request.method == 'POST':
        city.delete()
        return redirect('index')

    return render(request, 'city-delete.html', {'city': city})
