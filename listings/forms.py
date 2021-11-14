from django.forms import ModelForm

from .models import Listing


class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = [
            "title",
            "location",
            "price",
            "county",
            "property_type",
            "area",
            "bedrooms",
            "bathrooms",
            "car_spaces",
            "year",
            "photo_main",
            "photo_1",
            "photo_2",
            "photo_3",
            "photo_4",
            "photo_5",
            "photo_6",
        ]

        labels = {
            "title": "Naziv",
            "location": "Lokacija",
            "price": "Cijena (kn)",
            "county": "Županija",
            "area": "Stambena površina(m2)",
            "bedrooms": "Broj spavaćih soba",
            "bathrooms": "Broj kupaonica",
            "car_spaces": "Broj parkirnih mjesta",
            "property_type": "Tip objekta",
            "year": "Godina izgradnje",
            "photo_main": "Glavna slika",
            "photo_1": "Slika 1",
            "photo_2": "Slika 2",
            "photo_3": "Slika 3",
            "photo_4": "Slika 4",
            "photo_5": "Slika 5",
            "photo_6": "Slika 6",
        }
