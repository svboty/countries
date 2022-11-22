from django.shortcuts import render

from .helpers import Country

data = Country().data


def main_page(request):
    context = {}
    return render(request, 'main_page.html', context)


def countries_list(request):
    context = {
        "data": data
    }
    return render(request, 'countries_list.html', context)
