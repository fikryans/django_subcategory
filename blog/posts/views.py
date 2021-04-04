from django.shortcuts import render
from .models import Category


def show_category(request):
    show_cat = Category.objects.all()

    print(show_cat)

    context = {
        'show_cat':show_cat,
    }

    return render(request, 'index.html', context)

