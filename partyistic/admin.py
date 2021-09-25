from django.contrib import admin
# from nested_inline.admin import NestedStackedInline, NestedModelAdmin
from .models import Inspiration, Services, Parties, Cars, Places



# class PlacesInline(NestedStackedInline):
#     model = Places
#     extra = 1
#     fk_name = 'level'
   
# class CarsInline(NestedStackedInline):
#     model = Cars
#     extra = 1
#     fk_name = 'level'
#     inlines = [PlacesInline()]
# class ServicesAdmin(NestedModelAdmin):
#     model = Services
#     inlines = [CarsInline]

# Register your models here.
# admin.site.register(Cars)

# admin.site.register(Places)

admin.site.register(Inspiration)

admin.site.register(Services)

admin.site.register(Parties)
