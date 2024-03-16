from rest_framework import serializers
from videogames.models import VideoGames
class VideoGamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoGames
        fields = '__all__'