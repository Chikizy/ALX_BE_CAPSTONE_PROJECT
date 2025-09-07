from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .models import RentalListing
from .serializers import RentalListingSerializer

# Create your views here.

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # check whether request metho is a safe one
        # (does not alter records i.e is a read only method)
        #   if true(does not want to alter anything), allow request
        if request.method in permissions.SAFE_METHODS:
            return True
        # else if request is not safe, only allow alteration 
        # if requesting user is owner of specific listing
        return obj.owner == request.user
    
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

# Listing and create view:
class RentalListingListCreateView(generics.ListCreateAPIView):
    queryset = RentalListing.objects.all()
    serializer_class = RentalListingSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    # implement structured search; format <url>/?address=<location>
    filterset_fields = ['address', 'price_per_night']
    # implement keyword search; format: <url>/?search=<keyword>
    search_fields = ['title', 'description', 'address']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class RentalListingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RentalListing.objects.all()
    serializer_class = RentalListingSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]