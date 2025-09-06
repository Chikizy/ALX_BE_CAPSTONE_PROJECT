from rest_framework import serializers
from .models import RentalListing

class RentalListingSerializer(serializers.ModelSerializer):
    #owner = serializers.PrimaryKeyRelatedField(read_only=True)
    owner = serializers.SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        model = RentalListing
        fields = ['id', 'owner', 
                  'title', 'description', 
                  'address',
                  'price_per_night', 'availability_dates',
                #  'images',
                  'created_at', 'updated_at'
                  ]
        extra_kwargs = {
            'id': {'read_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }

        def validate_price_per_night(self, value):
            if value <= 0:
                raise serializers.ValidationError('Price must be set above zero')
            return value
        
        def validate_availability_dates(self, value):
            # check if dates are written in dict... format
            if not isinstance(value, dict) or 'start' not in value or 'end' not in value:
                raise serializers.ValidationError('Availability dates must be a dictionary having both "start" and "end" keys')
            return value