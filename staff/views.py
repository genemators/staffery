from django.contrib.postgres.search import SearchVector
from django.db.models import Q
from django.shortcuts import render
from .models import Employee
from .forms import SearchForm


def home(request):
    employees = Employee.objects.all()
    return render(request, 'home.html', {"employees": employees, "ceo": employees[0]})


def list(request):
    query = Employee.objects.all()

    sortKey = request.GET.get('sort')
    searchKey = request.GET.get('search')

    if sortKey is not None and sortKey in [f.name for f in Employee._meta.fields]:
        query.order_by(sortKey)

    if searchKey is not None:
        query.filter(
            Q(full_name__icontains=searchKey) | Q(position__icontains=searchKey) | Q(full_name__contains=searchKey) | Q(
                position__contains=searchKey)
        )
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            inp = form.cleaned_data['input']
            employees = Employee.objects.filter(
                Q(full_name__icontains=inp) | Q(position__icontains=inp) | Q(full_name__contains=inp) | Q(
                    position__contains=inp)
            )
            return render(request, 'sort.html', {"employees": employees, "form": form})
    else:
        form = SearchForm()
    return render(request, 'sort.html', {"employees": query, "form": form})
