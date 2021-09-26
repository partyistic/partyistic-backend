from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.postgres.fields import JSONField
# from django.db.models.JSONField import JSONField

# from django.contrib.postgres.fields import ArrayField

class Inspiration(models.Model):
    name = models.CharField(max_length=256)
    # images = models.cha
    description = models.TextField(default="", null=True, blank=True)

    def __str__(self):
        return self.name


class Services(models.Model):
    name = models.CharField(max_length=256)
    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True
    )
    type_choices = [('Places','Places'),('Planers','Planers'),('MusicBands','MusicBands'),('PhotoSession','PhotoSession'),('Fashion','Fashion'),('Cars','Cars'),('Trip','Trip')]
    service_type = models.CharField(max_length=64, choices = type_choices, default='Places')
    # description = models.TextField(default="", null=True, blank=True)

    def __str__(self):
        return self.name

class Places(models.Model):
    # service = models.ForeignKey(Services,on_delete= models.CASCADE)
    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True
    )
    name = models.CharField(max_length=256)
    description = models.TextField(default="", null=True, blank=True)
    # images = 
    location_link = models.CharField(max_length = 256)
    city_choices = [('Amman','Amman'),('Irbid','Irbid'),('Zarqa','Zarqa'),('Al-Mafraq','Al-Mafraq'),('Jarash','Jarash'),('Ajloun','Ajloun'),('As-Salt','As-Salt'),('Madaba','Madaba'),('karak','karak'),('Tafilah','Tafilah'),("Maan","Maan"),('Aqaba','Aqaba')]
    city = models.CharField(max_length=64, choices = city_choices, default='Amman')
    # price = 
    # strings = JSONField(models.CharField(max_length=50),default=list, blank=True, null=True)

    # skills = ArrayField(models.CharField(max_length=5, default=list, blank=True,null=True))
    # = ArrayField(
    #     ArrayField(
    #         models.CharField(max_length=10, blank=True),
    #         size=8,
    #     ),
    #     size=8,
    # )
    place_choices = [('Hall','Hall'),('Restaurant','Restaurant'),('Farm','Farm')]
    
    place_type = models.CharField(max_length=64, choices = place_choices, default='Hall')  
    # booked_dates =   
    def __str__(self):
        return self.name

class Cars(models.Model):
    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True
    )
    name = models.CharField(max_length=256)
   
    description = models.TextField(default="", null=True, blank=True)
    # service = models.ForeignKey(Services,on_delete= models.CASCADE)
    def __str__(self):
        return self.name


class Parties(models.Model):
    name = models.CharField(max_length=256)
    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True
    )
    description = models.TextField(default="", null=True, blank=True)

    def __str__(self):
        return self.name