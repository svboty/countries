from django.http import Http404
from django.shortcuts import render

from .helpers import Country

data = Country().data

alphabet = list('abcdefghijklmnopqrstuvwxyz')


def main_page(request):
    context = {}
    return render(request, 'main_page.html', context)


def countries_list(request):
    context = {
        "data": data,
        "alphabet": alphabet
    }
    return render(request, 'countries_list.html', context)


def country(request, name):
    for item in data:
        if item['country'].lower() == name.lower():
            context = {
                "country": item
            }
            return render(request, 'country.html', context)
    raise Http404(f'Страна "{name}" не найдена')


def country_by_letter(request, letter):
    countries = []
    for item in data:
        if item['country'].lower().startswith(letter.lower()):
            countries.append(item)
    context = {
        "data": countries,
        "alphabet": alphabet,
        "letter": letter
    }
    return render(request, 'countries_list.html', context)

