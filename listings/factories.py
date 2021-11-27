import random
import os

from faker import Faker
from factory.django import DjangoModelFactory, ImageField
from factory import LazyFunction
from factory.fuzzy import FuzzyChoice
from domonic.html import h2, br, h5

from accounts.models import CustomUser
from news.models import BlogPost
from news.choices import Category

from .models import Listing
from .choices import County, PropertyType

fake = Faker(locale='hr_HR')

def get_username():
    return f'{fake.user_name()}{random.randint(0,999)}'

def get_title_listing():
    return f'{fake.address()}'

def get_title_blog():
    return f'{fake.bs().title()}'

def get_text():
    return f'{fake.text()}'

def get_price():
    return f'{random.randint(700000, 2500000)}'

def get_area():
    return f'{random.randint(30, 150)}'

def get_int():
    return random.randint(1, 3)

def get_images():
    path = os.path.join(os.getcwd(), 'static/random_images')
    images = os.listdir(path)
    images = [f'static/random_images/{image}' for image in images]
    return images

def get_html():
    html = h2(fake.bs().title())
    for _ in range(random.randint(3,6)):
        html += br()
        html += h5(fake.paragraph(nb_sentences=random.randint(10,30)))
    return html

class UserFactory(DjangoModelFactory):
    class Meta:
        model = CustomUser

    username = LazyFunction(get_username)
    email = LazyFunction(fake.email)
    password = 'testing321'
    phone = LazyFunction(fake.phone_number)


class ListingFactory(DjangoModelFactory):
    class Meta:
        model = Listing

    title = LazyFunction(get_title_listing)
    author = FuzzyChoice(CustomUser.objects.all())
    location = LazyFunction(fake.address)
    price = LazyFunction(get_price)
    county = FuzzyChoice(x for x, _ in County.get_choices())
    area = LazyFunction(get_area)
    bedrooms = LazyFunction(get_int)
    bathrooms = LazyFunction(get_int)
    car_spaces = LazyFunction(get_int)
    property_type = FuzzyChoice(x for x, _ in PropertyType.get_choices())
    year = LazyFunction(fake.year)
    photo_main = ImageField(from_path=FuzzyChoice(img for img in get_images()))
    photo_1 = ImageField(from_path=FuzzyChoice(img for img in get_images()))
    photo_2 = ImageField(from_path=FuzzyChoice(img for img in get_images()))
    photo_3 = ImageField(from_path=FuzzyChoice(img for img in get_images()))
    photo_4 = ImageField(from_path=FuzzyChoice(img for img in get_images()))
    photo_5 = ImageField(from_path=FuzzyChoice(img for img in get_images()))
    photo_6 = ImageField(from_path=FuzzyChoice(img for img in get_images()))


class BlogPostFactory(DjangoModelFactory):
    class Meta:
        model = BlogPost

    title = LazyFunction(get_title_blog)
    lead = LazyFunction(get_text)
    image = ImageField(from_path=FuzzyChoice(img for img in get_images()))
    category = FuzzyChoice(x for x, _ in Category.get_choices())
    author = FuzzyChoice(CustomUser.objects.filter(is_staff=True))
    body = LazyFunction(get_html)
    is_published = True