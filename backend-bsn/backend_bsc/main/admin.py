from django.contrib import admin
from .models import Hauberge, Resident, BlackList, Reservation, HaubergeResident

admin.site.register(Hauberge)
admin.site.register(Resident)
admin.site.register(BlackList)
admin.site.register(Reservation)
admin.site.register(HaubergeResident)
