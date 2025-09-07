from django.urls import path
from .views import RentalListingListCreateView, RentalListingDetailView

urlpatterns = [
    # path is included in project urls.py, so endpoint 
    path('', RentalListingListCreateView.as_view(), name='listing-list-create'),
    path('listingdetails/', RentalListingDetailView.as_view(), name='listing-detail'),
]