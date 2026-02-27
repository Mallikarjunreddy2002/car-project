from django.shortcuts import render, redirect, get_object_or_404
from .models import Car
from .forms import CarForm

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'car_list.html', {'cars': cars})

def car_create(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('car_list')
    else:
        form = CarForm()
    return render(request, 'car_form.html', {'form': form})

def car_update(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == 'POST':
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('car_list')
    else:
        form = CarForm(instance=car)
    return render(request, 'car_form.html', {'form': form})

def car_delete(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == 'POST':
        car.delete()
        return redirect('car_list')
    return render(request, 'car_confirm_delete.html', {'car': car})
