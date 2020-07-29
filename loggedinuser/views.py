from loggedinuser.models import Post
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import Postserializer
from .models import Post
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.decorators import api_view ,permission_classes
# Create your views here.


@login_required()
def userhome(request):
    return render(request, "loggedin/posts.html")



''' def get(self, request):
        post = Post.objects.all()
        serialize = Postserializer(post,many=True)
        return Response(serialize.data)

    
    def post(self,request):
        serializer = Postserializer(data=request.data)
        print("helohelo")
        if serializer.is_valid():
            
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
'''




@permission_classes((IsAuthenticated, ))
@api_view(['GET', 'POST', 'DELETE'])
def Post_list(request):
    if request.method == 'GET':
        post = Post.objects.all()
        serialize = Postserializer(post,many=True)
        return JsonResponse(serialize.data, safe=False)
            # 'safe=False' for objects serialization
    elif request.method == 'POST':
        serializer = Postserializer(data=request.data)
       
        if serializer.is_valid():   
            serializer.save()
            print(serializer.save())
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED,safe=True)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST,safe=True)
        
      #  elif request.method == 'DELETE':
      #      count = Tutorial.objects.all().delete()
       #     return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

            