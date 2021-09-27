from django.urls import path
from .views import InspirationList,InspirationDetail, PartiesList, PartiesDetail, PlacesList, PlacesDetail,PlannersList,PlannersDetail, MusicBandsList, MusicBandsDetail, PhotoSessionsList, PhotoSessionsDetail, FashionList, FashionDetail, CarsList, CarsDetail, TripsList, TripsDetail

urlpatterns = [
    path("inspiration/", InspirationList.as_view(), name="inspiration_list"),
    path("inspiration/<int:pk>/", InspirationDetail.as_view(), name="inspiration_detail"),

    # path("services/", ServicesList.as_view(), name="services_list"),
    # path("services/<int:pk>/", ServicesDetail.as_view(), name="services_detail"),

    path("places/", PlacesList.as_view(), name="places_list"),
    path("places/<int:pk>/", PlacesDetail.as_view(), name="places_detail"),

    path("planners/", PlannersList.as_view(), name="planners_list"),
    path("planners/<int:pk>/", PlannersDetail.as_view(), name="planners_detail"),

    path("musicbands/", MusicBandsList.as_view(), name="musicbands_list"),
    path("musicbands/<int:pk>/", MusicBandsDetail.as_view(), name="musicbands_detail"),

    path("photosessions/", PhotoSessionsList.as_view(), name="photosessions_list"),
    path("photosessions/<int:pk>/", PhotoSessionsDetail.as_view(), name="photosessions_detail"),

    path("fashion/", FashionList.as_view(), name="fashion_list"),
    path("fashion/<int:pk>/", FashionDetail.as_view(), name="fashion_detail"),

    path("cars/", CarsList.as_view(), name="cars_list"),
    path("cars/<int:pk>/", CarsDetail.as_view(), name="cars_detail"),

    path("trips/", TripsList.as_view(), name="trips_list"),
    path("trips/<int:pk>/", TripsDetail.as_view(), name="trips_detail"),

    path("parties/", PartiesList.as_view(), name="parties_list"),
    path("parties/<int:pk>/", PartiesDetail.as_view(), name="parties_detail"),
]
