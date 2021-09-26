from django.contrib import admin
# from nested_inline.admin import NestedStackedInline, NestedModelAdmin
from .models import Inspiration, Places, Planners, MusicBands ,PhotoSession, Fashion, Cars, Trip, Parties

admin.site.register(Inspiration)

# admin.site.register(Services)
admin.site.register(Places)
admin.site.register(Planners)
admin.site.register(MusicBands)
admin.site.register(PhotoSession)
admin.site.register(Fashion)
admin.site.register(Cars)
admin.site.register(Trip)

admin.site.register(Parties)
