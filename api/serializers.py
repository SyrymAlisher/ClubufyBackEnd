from rest_framework import serializers
from api.models import Category, Club
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = 'id', 'name'

class ClubSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField()
    img = serializers.CharField()
    text = serializers.CharField()
    desc = serializers.CharField()
    category = CategorySerializer()