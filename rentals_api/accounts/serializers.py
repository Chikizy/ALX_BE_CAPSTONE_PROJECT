from rest_framework import serializers
from .models import CustomUser
from rest_framework.authtoken.models import Token

def validate_role(value):
#   validate if role is owner or renter
    valid_roles = [choice[0] for choice in CustomUser.ROLE_CHOICES]
    if value not in valid_roles:
        raise serializers.ValidationError("Ensure Role is 'Owner' or 'Renter'.")
    return value
    
class UserRegistrationSerializer(serializers.ModelSerializer):
    # serialise password making it write ony to avoid exposure
    password = serializers.CharField(write_only=True)
    role = serializers.CharField(validators=[validate_role])

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'role', 'contact_info']
        extra_kwargs = {
            'password' : {'write_only':True},
            'id' : {'read_only':True},
            }
        
    def create(self, validated_data):
        user = CustomUser.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        #    password=validated_data['password'],
            role=validated_data['role'],
        #   use .get because the field(contact_info) is optional, may not exist in the request
        #   .get(<'key'>, <'defaukt'>)
            contact_info=validated_data.get('contact_info', '')
        )
        #   hash the password
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

            
    