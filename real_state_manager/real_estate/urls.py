from django.urls import path

from real_state_manager.real_estate.api.views import PropertyView

app_name = "real_estate"

urlpatterns = [
    path("properties/", PropertyView.as_view(), name="property_list"),
    # path("properties/<int:pk>/", PropertyDetailView.as_view(), name="property_detail"),
    # path("properties/create/", PropertyCreateView.as_view(), name="property_create"),
    # path("properties/<int:pk>/update/", PropertyUpdateView.as_view(), name="property_update"),
    # path("properties/<int:pk>/delete/", PropertyDeleteView.as_view(), name="property_delete"),
]
