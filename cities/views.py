from django.shortcuts import render, redirect
from .models import Region
from .forms import RegionForm


def index(request):
    regions = Region.objects.all()
    return render(request, 'index.html', {'regions': regions})


def new_region(request):
    form = RegionForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request, 'regions-form.html', {'form': form})


def update_region(request, id):
    region = Region.objects.get(id=id)
    form = RegionForm(request.POST or None, instance=region)

    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request, 'regions-form.html', {'form': form, 'region': region})


def delete_region(request, id):
    region = Region.objects.get(id=id)
    print('>>>>>>', request)
    if request.method == 'POST':
        region.delete()
        return redirect('index')

    return render(request, 'region-delete.html', {'region': region})
