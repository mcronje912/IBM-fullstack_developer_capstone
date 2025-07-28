from django.contrib import admin
from .models import CarMake, CarModel

# Register your models here.


# CarModelInline class
class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 3


# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    list_display = ['car_make', 'name', 'type', 'year', 'dealer_id']
    list_filter = ['type', 'car_make', 'year']
    search_fields = ['car_make__name', 'name']


# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
    list_display = ['name', 'description']
    search_fields = ['name']


# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
