from loggedinuser.models import Post
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import Postserializer
from .models import Post

# Create your views here.


@login_required()
def userhome(request):
    return render(request, "loggedin/posts.html")


class Post_list(APIView):
    def get(self, request):
        post = Post.objects.all()
        serialize = Postserializer(post,many=True)
        return Response(serialize.data)

    '''def post(self, request):
        pass'''
    def post(self,request):
        serializer = Postserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)