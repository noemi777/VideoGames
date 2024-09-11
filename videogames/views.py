from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from videogames.models import VideoGames
from videogames.serializers import VideoGamesSerializer

# Create your views here.

class CreateGame(APIView):
    permission_classes = (AllowAny, )

    def post(self, request):
        serializer = VideoGamesSerializer(data=request.data)
        if  serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message': 'Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ReadListGames(APIView):
    permission_classes = (AllowAny, )

    def get(self, request):
        try:
            game_obj = VideoGames.objects.all()
            serializer = VideoGamesSerializer(game_obj, many=True)
            return Response (serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({'message':'Not Found'},status=status.HTTP_400_BAD_REQUEST)
    
class ReadGamesId(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, id):
        try:
            game_obj = VideoGames.objects.get(pk=id)
            serializer = VideoGamesSerializer(game_obj)
            return Response(serializer.data)
        except:
            return Response({'message':'No encontrado'},status=status.HTTP_400_BAD_REQUEST)
    
