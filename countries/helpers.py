import json
import pathlib
from .models import Country, Language


class CountryFile(object):
    data = None

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(CountryFile, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        if not self.data:
            path = pathlib.Path(pathlib.Path.cwd(), 'country-by-languages.json')
            with open(path, 'r') as file:
                self.data = json.load(file)


def load_data():
    data = CountryFile().data
    for item in data:
        country = Country.objects.create(name=item['country'])
        languages = []
        for lang in item['languages']:
            lang_in_db, _ = Language.objects.get_or_create(label=lang)
            languages.append(lang_in_db)
        country.languages.set(languages)
