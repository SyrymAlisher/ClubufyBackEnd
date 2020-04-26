from rest_framework import serializers
from api.models import Category, Club, Manager, Enrollment
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = 'id', 'name'

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = 'id', 'username', 'password'

class ClubSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField()
    img = serializers.CharField()
    text = serializers.CharField()
    desc = serializers.CharField()
    category = CategorySerializer()

class EnrollmentSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField()
    phone = serializers.CharField()
    club = ClubSerializer()

