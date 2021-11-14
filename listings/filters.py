import django_filters as filters
from django_filters.widgets import RangeWidget,CSVWidget,DateRangeWidget

from .models import Listing


class ListingFilter(filters.FilterSet):
    def __init__(self, *args, **kwargs):
       super(ListingFilter, self).__init__(*args, **kwargs)
       self.filters['county'].label="Županija"
       self.filters['property_type'].label="Tip objekta"
       self.filters['price'].label="Cijena u kunama (min - max)"
       self.filters['year'].label="Godina izgradnje (min - max)"
       self.filters['area'].label="Stambena površina (min - max)"
       self.filters['bedrooms'].label="Broj spavaćih soba (min - max)"
       self.filters['bathrooms'].label="Broj kupaonica (min - max)"
       self.filters['car_spaces'].label="Broj parkirnih mjesta (min - max)"

    price = filters.RangeFilter()
    year = filters.RangeFilter()
    area = filters.RangeFilter()
    bedrooms = filters.RangeFilter()
    bathrooms = filters.RangeFilter()
    car_spaces = filters.RangeFilter()


    class Meta:
        model = Listing
        fields = ["county", "property_type"]

        