from post.models import Post, PostFile
from rest_framework import serializers

class PostFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostFile
        exclude = ['post']


class PostSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    files = PostFileSerializer(many=True, read_only=True)
    likes = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Post
        fields = '__all__'

    def get_likes(self, obj):
        return obj.like_set.count()
    
    def get_files(self, obj):
        return obj.files.all()
    