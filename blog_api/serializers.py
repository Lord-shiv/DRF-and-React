from rest_framework import serializers
from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'author', 'excerpt',
<<<<<<< HEAD
                  'content', 'status')
=======
                  'content', 'published', 'status')
>>>>>>> 88b93d8ad65f36207ff349cbcb22e4c95c300e19
        model = Post
