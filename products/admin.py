from django.contrib import admin
from .models import Phone, Tab, Watch, Airpod, AirpodsCover,  PhonesCover, TabsCover, WatchesCover, PhoneRate, TabRate, WatchRate, AirpodRate

# Register your models here.
admin.site.register(Phone)
admin.site.register(Tab)
admin.site.register(Watch)
admin.site.register(Airpod)
admin.site.register(AirpodsCover)
admin.site.register(PhonesCover)
admin.site.register(TabsCover)
admin.site.register(WatchesCover)
admin.site.register(PhoneRate)
admin.site.register(TabRate)
admin.site.register(WatchRate)
admin.site.register(AirpodRate)
