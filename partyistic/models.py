from django.contrib.auth import get_user_model
from django.db import models
# from django.contrib.postgres.fields import JSONField
# from django.db.models.JSONField import JSONField
# from django.contrib.postgres.fields import ArrayField

# Inspiration, Places, Planners, MusicBands ,PhotoSession, Fashion, Cars, Trip, Parties

class Inspiration(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(default="", null=True, blank=True)
    images = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.name


# class Services(models.Model):
    # name = models.CharField(max_length=256)
    # owner = models.ForeignKey(
    #     get_user_model(), on_delete=models.CASCADE, null=True, blank=True
    # )
    # type_choices = [('Places','Places'),('Planners','Planners'),('MusicBands','MusicBands'),('PhotoSession','PhotoSession'),('Fashion','Fashion'),('Cars','Cars'),('Trip','Trip')]
    # service_type = models.CharField(max_length=64, choices = type_choices, default='Places')
    # # description = models.TextField(default="", null=True, blank=True)

    # def __str__(self):
    #     return self.name

class Places(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=256)
    description = models.TextField(default="", null=True, blank=True)
    images = models.JSONField(blank=True, null=True)
    location_link = models.CharField(max_length = 256)
    city = models.CharField(max_length=64, choices = [('Amman','Amman'),('Irbid','Irbid'),('Zarqa','Zarqa'),('Al-Mafraq','Al-Mafraq'),('Jarash','Jarash'),('Ajloun','Ajloun'),('As-Salt','As-Salt'),('Madaba','Madaba'),('karak','karak'),('Tafilah','Tafilah'),("Maan","Maan"),('Aqaba','Aqaba')], default='Amman')
    price = models.IntegerField()
    reviews = models.JSONField(blank=True, null=True)
    place_type = models.CharField(max_length=64, choices = [('Hall','Hall'),('Restaurant','Restaurant'),('Farm','Farm')], default='Hall')  
    booked_dates = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.name

class Planners(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=256)
    description = models.TextField(default="", null=True, blank=True)
    images = models.JSONField(blank=True, null=True)
    price = models.IntegerField()
    reviews = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.name

class MusicBands(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=256)
    description = models.TextField(default="", null=True, blank=True)
    images = models.JSONField(blank=True, null=True)
    price = models.IntegerField()
    reviews = models.JSONField(blank=True, null=True)
    booked_dates = models.JSONField(blank=True, null=True)

class PhotoSession(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=256)
    description = models.TextField(default="", null=True, blank=True)
    images = models.JSONField(blank=True, null=True)
    price = models.IntegerField()
    reviews = models.JSONField(blank=True, null=True)
    booked_dates = models.JSONField(blank=True, null=True)

class Fashion(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=256)
    description = models.TextField(default="", null=True, blank=True)
    images = models.JSONField(blank=True, null=True)
    location_link = models.CharField(max_length = 256)
    city = models.CharField(max_length=64, choices = [('Amman','Amman'),('Irbid','Irbid'),('Zarqa','Zarqa'),('Al-Mafraq','Al-Mafraq'),('Jarash','Jarash'),('Ajloun','Ajloun'),('As-Salt','As-Salt'),('Madaba','Madaba'),('karak','karak'),('Tafilah','Tafilah'),("Maan","Maan"),('Aqaba','Aqaba')], default='Amman')
    price = models.IntegerField()
    reviews = models.JSONField(blank=True, null=True)
class Cars(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=256)
    description = models.TextField(default="", null=True, blank=True)
    images = models.JSONField(blank=True, null=True)
    location_link = models.CharField(max_length = 256)
    city = models.CharField(max_length=64, choices = [('Amman','Amman'),('Irbid','Irbid'),('Zarqa','Zarqa'),('Al-Mafraq','Al-Mafraq'),('Jarash','Jarash'),('Ajloun','Ajloun'),('As-Salt','As-Salt'),('Madaba','Madaba'),('karak','karak'),('Tafilah','Tafilah'),("Maan","Maan"),('Aqaba','Aqaba')], default='Amman')
    price = models.IntegerField()
    reviews = models.JSONField(blank=True, null=True)
    booked_dates = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.name

class Trip(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=256)
    description = models.TextField(default="", null=True, blank=True)
    images = models.JSONField(blank=True, null=True)
    price = models.IntegerField()
    reviews = models.JSONField(blank=True, null=True)

class Parties(models.Model):
    name = models.CharField(max_length=256)
    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True
    )
    description = models.TextField(default="", null=True, blank=True)

    def __str__(self):
        return self.name