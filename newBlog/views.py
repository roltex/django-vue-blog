from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Blog
from .serializers import BlogSerializer

class BlogListAPIView(APIView):
    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True, context={'request': request})
        return Response(serializer.data)

class BlogDetailAPIView(APIView):
    def get(self, request, pk, *args, **kwargs):
        try:
            blog = Blog.objects.get(pk=pk)  # Fetch the blog by primary key
        except Blog.DoesNotExist:
            raise NotFound("Blog not found")  # Raise a 404 error if not found
        serializer = BlogSerializer(blog, context={'request': request})
        return Response(serializer.data)  # Return the serialized data