from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response

from api.serializers import CategorySerializer, ClubSerializer, ManagerSerializer, EnrollmentSerializer
from api.models import Category, Club, Manager, Enrollment

from rest_framework.permissions import IsAuthenticated

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

@api_view(['GET'])
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

    elif request.method == 'POST':
        try:
            category = Category.objects.get(name=request.data['category2'])
            author = Manager.objects.get(username=request.data['author2'])
            Club.objects.create(
                name = request.data['name'],
                img = request.data['img'],
                text = request.data['text'],
                desc = request.data['desc'],
                category = category,
                author = author
            )
            return JsonResponse({"succ": "created club"}, safe=False)
        except:
            return JsonResponse({"error": "error creating club"}, safe=False)


@api_view(['GET', 'PUT', 'DELETE'])
def club(request, id):
    permission_classes = (IsAuthenticated,)
    try:
        club = Club.objects.get(id=id)
    except:
        return JsonResponse({'error': 'cant get club'}, safe=False)
    
    if request.method == 'GET':
        serializer = ClubSerializer(club)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'PUT':
        try:
            category = Category.objects.get(name=request.data['category2'])
            author = Manager.objects.get(username=request.data['author2'])
        except:
            return JsonResponse({'error': 'cant get that categry'}, safe=False)
        
        club.name = request.data['name']
        club.img = request.data['img']
        club.text = request.data['text']
        club.desc = request.data['desc']
        club.category = category
        club.author = author
        club.save()
        return JsonResponse({'success': 'update club successfully'}, safe=False)
    
    elif request.method == 'DELETE':
        club.delete()
        return JsonResponse({'eror': 'deleted'}, safe=False)

class EnrollmentView(APIView):
    def post(self, request):
        try:
            club = Club.objects.get(id=request.data['club_id'])
        except:
            return JsonResponse({'errior': 'cant get club'}, safe=False)

        Enrollment.objects.create(
            name = request.data['name'],
            phone = request.data['phone'],
            club = club
        )

        return JsonResponse({"success": "enrolled"}, safe=False)

    def get(self, request):
        try:
            enrolls = Enrollment.objects.all()
            serializer = EnrollmentSerializer(enrolls, many=True)
            return JsonResponse(serializer.data, safe=False)
        except:
            return JsonResponse(serializer.errors, safe=False)