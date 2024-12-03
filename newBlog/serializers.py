from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    main_image = serializers.SerializerMethodField()  # Add this for absolute URL

    class Meta:
        model = Blog
        fields = ['id', 'title', 'description', 'main_image', 'created_at', 'author']

    def get_main_image(self, obj):
        request = self.context.get('request')
        if obj.main_image:
            return request.build_absolute_uri(obj.main_image.url)
        return None
