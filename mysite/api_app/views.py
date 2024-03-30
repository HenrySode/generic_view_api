from django.shortcuts import render
from requests import Response
from rest_framework import generics, status
from . models import BlogPost
from .serializers import BlogPostSerializer
from rest_framework.views import APIView 

class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    
    def delete(self, request, *args, **kwargs):
        object = BlogPost.objects.all()
        object.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


class BlogPostRetreiveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = "pk"


class BlogPostList(APIView): 
    def get(self, request, format=None):
        title = request.query_params.get("title","")

        if title:
            blog_posts = BlogPost.objects.filter(title_icontains=title)
        else:
            blog_posts = BlogPost.objects.all()

        serializer = BlogPostSerializer(blog_posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)