from django.db import models
from django.contrib.gis.db import models
from django_pgjson.fields import JsonBField
from django.contrib.postgres.fields import ArrayField


AirportTypes = (
    ('airport', 'airport'),
    ('railway', 'railway'),
    ('heliport', 'heliport'),
    ('bus', 'bus'),
    ('harbour', 'harbour'),
    ('military', 'military'),
    ('seaplane', 'seaplane')
)

class Aircraft(models.Model):
    _id = models.CharField(max_length=255, default='', unique=True, db_index=True)
    name = models.TextField()
    seats = models.IntegerField(null=True)
    wide_body = models.BooleanField(default=False)

class Place(models.Model):
    _id = models.CharField(max_length=255, default='', unique=True, db_index=True)
    code = models.CharField(max_length=3)
    name = JsonBField()
    weight = JsonBField()
    coordinates = models.PointField(null=True)
    flightable = models.BooleanField(default=False)

class City(Place):
    pass

class Country(Place):
    pass

class Airport(Place):
    type = models.CharField(max_length=255, choices=AirportTypes)


class SpecialOffer(models.Model):
    title = models.TextField()
    _id = models.CharField(max_length=255, default='', unique=True, db_index=True)
    airline_mongo_id = models.CharField(max_length=255, default='', db_index=True)
    start_date = models.DateTimeField(null=True)
    finish_date = models.DateTimeField(null=True)
    flight_start_date = models.DateTimeField(null=True)
    flight_finish_date = models.DateTimeField(null=True)
    description = models.TextField(null=True, blank=True)
    archive = ArrayField(models.CharField(max_length=255),null=True)
    external_url = models.CharField(max_length=255, null=True, blank=True)
    host = models.CharField(max_length=255, null=True, blank=True)
    slug_cache = models.CharField(max_length=255, null=True, blank=True)
    price = models.CharField(max_length=255, null=True, blank=True)
    expired = models.BooleanField(default=False)

    
class Route(models.Model):
    _id = models.CharField(max_length=255, default='', unique=True, db_index=True)
    airline_mongo_ids = ArrayField(models.CharField(max_length=255), null=True)
    created_at = models.DateTimeField()  # auto_now_add=True
    updated_at = models.DateTimeField()  # auto_now=True
    dest_mongo_id = models.CharField(max_length=255)
    orig_mongo_id = models.CharField(max_length=255)
    max_duration = models.BigIntegerField(null=True)
    min_duration = models.BigIntegerField(null=True)
    weight = JsonBField()

class CountryRoute(Route):
    pass

class CityAirportRoute(Route):
    pass

class AirportCityRoute(Route):
    pass

class CityRoute(Route):
    aviasales_path = models.TextField()


class FlightCode(models.Model):
    _id = models.CharField(max_length=255, default='', unique=True, db_index=True)
    aircraft_mongo_ids = ArrayField(models.CharField(max_length=255), null=True)
    created_at = models.DateTimeField(null=True)  # auto_now_add=True
    updated_at = models.DateTimeField(null=True)  # auto_now=True
    first_date = models.DateTimeField(null=True)
    last_date = models.DateTimeField(null=True)
    airline_mongo_id = models.CharField(max_length=255)
    flight_number = models.CharField(max_length=255)
    aircraft = models.CharField(max_length=255, null=True)
    airport_route_mongo_id = models.CharField(max_length=255)
    weight = JsonBField()
    durations = ArrayField(models.IntegerField(), null=True)
    duration = models.IntegerField(null=True)
    

class Airline(models.Model):
    _id = models.CharField(max_length=255, default='', unique=True, db_index=True)
    main_color = models.CharField(max_length=255, null=True)
    additional_color = models.CharField(max_length=255, null=True)
    phone_number = models.CharField(max_length=255, null=True)
    website_address = models.CharField(max_length=255, null=True)
    address = models.TextField(null=True, blank=True)
    pending_destroy = models.BooleanField(default=False)
    online_checkin_address = models.TextField(null=True, blank=True)
    aviasales_path = models.TextField(null=True, blank=True)
    code = models.CharField(max_length=3, null=False, blank=False)
    alliance_mongo_id = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(null=True)  # auto_now_add=True
    updated_at = models.DateTimeField(null=True)  # auto_now=True
    iata_name = ArrayField(models.CharField(max_length=255), null=True)
    pending_iata_name = ArrayField(models.CharField(max_length=255), null=True)
    weight = JsonBField()
    name = JsonBField(default={})
    description = JsonBField(default={})
