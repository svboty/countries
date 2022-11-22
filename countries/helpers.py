import json
import pathlib


class Country(object):
    data = None

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Country, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        if not self.data:
            path = pathlib.Path(pathlib.Path.cwd(), 'country-by-languages.json')
            with open(path, 'r') as file:
                self.data = json.load(file)
