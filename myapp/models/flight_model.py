import datetime

import django.utils.timezone
from myapp.models.airline_model import Airline
from django.db import models


class Flight(models.Model):
    origin = models.CharField(max_length=100, null=False)
    destination = models.CharField(max_length=100, null=False)
    date = models.DateField(default=datetime.date.today)
    take_off_time = models.TimeField(null=False)
    landing_time = models.TimeField(null=False)
    seats_number = models.IntegerField(null=False, default=100)
    owner = models.ForeignKey(Airline, on_delete=models.CASCADE)
    price = models.IntegerField(null=False)

    @classmethod
    def get_date_flights(cls, date: datetime.datetime):
        return list(Flight.objects.filter(date=date).id)

    @classmethod
    def get_airline(cls, flight_id):
        return Flight.objects.get(id=flight_id).owner.id

    @classmethod
    def get_seats_number(cls, flight_id):
        return Flight.objects.get(id=flight_id).seats_number

    @classmethod
    def search_flight(cls, origin, destination, date):
        return list(Flight.objects.filter(origin=origin, destination=destination, date=date).id)

    @classmethod
    def get_price(cls, flight_id):
        return Flight.objects.get(id=flight_id).price
