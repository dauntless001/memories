from rest_framework import viewsets
from like.api.serializers import LikeSerializer
from like.models import Like

class LikeViewSet(viewsets.ModelViewSet):
    serializer_class = LikeSerializer
    queryset = Like.objects.all()