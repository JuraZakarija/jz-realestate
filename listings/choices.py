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

class County(EnumMixin):
    Zagrebačka = "Zagrebačka"
    Krapinsko_zagorska = "Krapinsko-zagorska"
    Sisačko_moslavačka = "Sisačko-moslavačka"
    Karlovačka = "Karlovačka"
    Varaždinska = "Varaždinska"
    Koprivničko_križevačka = "Koprivničko-križevačka"
    Bjelovarsko_bilogorska = "Bjelovarsko-bilogorska"
    Primorsko_goranska = "Primorsko-goranska"
    Ličko_senjska = "Ličko-senjska"
    Virovitičko_podravska = "Virovitičko-podravska"
    Požeško_slavonska = "Požeško-slavonska"
    Brodsko_posavska = "Brodsko-posavska"
    Zadarska = "Zadarska"
    Osječko_baranjska = "Osječko-baranjska"
    Šibensko_kninska = "Šibensko-kninska"
    Vukovarsko_srijemska = "Vukovarsko-srijemska"
    Splitsko_dalmatinska = "Splitsko-dalmatinska"
    Istarska = "Istarska"
    Dubrovačko_neretvanska = "Dubrovačko-neretvanska"
    Međimurska = "Međimurska"
    Grad_Zagreb = "Grad Zagreb"


class PropertyType(EnumMixin):
    Stan = "Stan"
    Kuća = "Kuća"
    Apartman = "Apartman"
    Poslovni_prostor = "Poslovni prostor"
