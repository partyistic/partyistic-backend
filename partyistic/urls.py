from django.urls import path
from .views import InspirationList,InspirationDetail, ServicesList, ServicesDetail, PartiesList, PartiesDetail

urlpatterns = [
    path("inspiration/", InspirationList.as_view(), name="inspiration_list"),
    path("inspiration/<int:pk>/", InspirationDetail.as_view(), name="inspiration_detail"),

    path("services/", ServicesList.as_view(), name="services_list"),
    path("services/<int:pk>/", ServicesDetail.as_view(), name="services_detail"),

    path("parties/", PartiesList.as_view(), name="parties_list"),
    path("arties/<int:pk>/", PartiesDetail.as_view(), name="parties_detail"),
]
