from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from api.serializers import CategorySerializer, ClubSerializer
from api.models import Category, Club

def first(request):
    return JsonResponse({"hello": "first view message"}, safe=False)

class CategoriesView(APIView):
    def get(self, request):
        try:
            categories = Category.objects.all()
            serializer = CategorySerializer(categories, many=True)
            return JsonResponse(serializer.data, safe=False)
        except:
            return JsonResponse(serializer.errors, safe=False)
    
    def post(self, request):
        try:
            Category.objects.create(
                name = request.data['name']
            )
            return JsonResponse({"success": "created category"}, safe=False)
        except:
            return JsonResponse({"error": "error creating category"}, safe=False)

@api_view(['GET', 'POST'])
def clubs_by_category(request, id):
    if request.method == 'GET':
        try:
            category = Category.objects.get(id=id)
            clubs = category.club_set.all()
            serializer = ClubSerializer(clubs, many=True)
            return JsonResponse(serializer.data, safe=False)
        except:
            return JsonResponse(serializer.erros, safe=False)

@api_view(['GET', 'POST'])
def clubs(request):
    if request.method == 'GET':
        try:
            clubs = Club.objects.all()
            serializer = ClubSerializer(clubs, many=True)
            return JsonResponse(serializer.data, safe=False)
        except:
            return JsonResponse(serializer.erros, safe=False)

