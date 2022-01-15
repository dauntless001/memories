from rest_framework import viewsets
from post.api.serializers import PostSerializer
from post.models import Post

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()