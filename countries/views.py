import logging

from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import get_object_or_404, render

from countries.models import Country, Language


logger = logging.getLogger(__name__)

alphabet = list('abcdefghijklmnopqrstuvwxyz')


def main_page(request):
    context = {}
    return render(request, 'main_page.html', context)


def countries_list(request):
    data_all = Country.objects.all().order_by('name')
    paginator = Paginator(data_all, 10)

    page_number = request.GET.get('page')
    data_page = paginator.get_page(page_number)
    context = {
        "data": data_page,
        "alphabet": alphabet
    }
    return render(request, 'countries_list.html', context)


def country(request, id):
    item = get_object_or_404(Country, id=id)
    context = {
        "country": item
    }
    return render(request, 'country.html', context)


def country_by_letter(request, letter):
    countries = Country.objects.filter(name__istartswith=letter)
    context = {
        "data": countries,
        "alphabet": alphabet,
        "letter": letter
    }
    return render(request, 'countries_list.html', context)


def languages_list(request):
    languages = Language.objects.all().order_by('label')
    context = {
        "languages": languages
    }
    return render(request, 'languages_list.html', context)


def language(request, id):
    lang = get_object_or_404(Language, id=id)
    countries = Country.objects.filter(languages=lang)
    context = {
        "language": lang,
        "countries": countries
    }
    return render(request, 'language.html', context)
