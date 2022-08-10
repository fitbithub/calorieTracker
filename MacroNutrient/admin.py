from django.contrib import admin
from .models import Food, Consume
# Register your models here.
admin.site.site_title = "Calories Tracker"
admin.site.site_header = "Calories Tracker"
admin.site.register(Food)
admin.site.register(Consume)