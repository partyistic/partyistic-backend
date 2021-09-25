from django.contrib import admin
from .models import Inspiration, Services, Parties

# Register your models here.
admin.site.register(Inspiration)

admin.site.register(Services)

admin.site.register(Parties)
