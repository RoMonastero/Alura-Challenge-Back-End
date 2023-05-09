from rest_framework import serializers
from aluraflix.models import Video
from aluraflix.validators import *

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

    def validate(self, data):
        if(not valida_url(data['url'])):
            raise serializers.ValidationError({'url':"URL inválida"})
        return data