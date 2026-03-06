from django.contrib import admin

from station.models import Bus, Order, Facility, Ticket, Trip

admin.site.register(Bus)
admin.site.register(Order)
admin.site.register(Facility)
admin.site.register(Ticket)
admin.site.register(Trip)

