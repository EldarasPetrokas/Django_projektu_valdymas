from django.shortcuts import render, get_object_or_404, redirect
from .models import Darbas, Darbuotojas, Klientas, Projektas, Saskaita
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after registration
            return redirect('index')  # Redirect to the home page
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def projektai_list(request):

    projektai = Projektas.objects.filter(vadovas=request.user)

    # Paginate the projects list
    paginator = Paginator(projektai, 5)  # Show 5 projects per page
    page = request.GET.get('page')
    try:
        projektai_paginated = paginator.page(page)
    except PageNotAnInteger:
        projektai_paginated = paginator.page(1)  # If page is not an integer, deliver the first page
    except EmptyPage:
        projektai_paginated = paginator.page(paginator.num_pages)  # If page is out of range, deliver the last page

    return render(request, 'projektai_list.html', {'projektai': projektai_paginated})


def projektas_detail(request, pk):
    projektas = get_object_or_404(Projektas, pk=pk)
    return render(request, 'projektas_detail.html', {'projektas': projektas})
