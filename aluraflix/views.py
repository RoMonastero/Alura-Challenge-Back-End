from rest_framework import viewsets, generics, status
from aluraflix.models import Video
from aluraflix.serializer import VideoSerializer
from rest_framework.response import Response

class VideosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os vídeos"""
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
    
        return Response({'message': 'Vídeo removido com sucesso'}, status=status.HTTP_204_NO_CONTENT)