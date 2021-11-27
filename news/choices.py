from enum import Enum


class EnumMixin(Enum):
    
    @classmethod
    def get_choices(items):
        return((item.name, item.value) for item in items)

    @classmethod
    def get_value(items, name):
        try:
            return items[name].get_value
        except KeyError:
            return ""


class Category(EnumMixin):
    Novogradnja = "Novogradnja"
    Aktualno = "Aktualno"
    Savjeti = "Savjeti"
    Hrvatska = "Hrvatska"
    Svijet = "Svijet"

