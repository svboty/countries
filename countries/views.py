from django.http import Http404
from django.core.paginator import Paginator
from django.shortcuts import render

from .helpers import Country
import logging

logger = logging.getLogger(__name__)

data = Country().data

alphabet = list('abcdefghijklmnopqrstuvwxyz')


def main_page(request):
    context = {}
    return render(request, 'main_page.html', context)


def countries_list(request):
    data_all = data
    paginator = Paginator(data_all, 10)

    page_number = request.GET.get('page')
    data_page = paginator.get_page(page_number)
    context = {
        "data": data_page,
        "alphabet": alphabet
    }
    logger.error(data_page)
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


def languages_list(request):
    languages = []
    for item in data:
        languages.extend(item['languages'])
    languages.sort()
    context = {
        "languages": set(languages)
    }
    return render(request, 'languages_list.html', context)


def language(request, lang):
    countries = []
    for item in data:
        if lang in item['languages']:
            countries.append(item['country'])
    countries.sort()
    context = {
        "language": lang,
        "countries": countries
    }
    return render(request, 'language.html', context)
