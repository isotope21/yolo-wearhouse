# import viewsets
from rest_framework import viewsets

# import local data
from .serializers import GeeksSerializer
from .models import GeeksModel
from sample import predict


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from snippets.models import Snippet
# from yoloapi.serializers import SnippetSerializer
from yoloapi import models

# @csrf_except
@api_view(['GET', 'POST'])
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        # snippets = Snippet.objects.all()
        # serializer = SnippetSerializer(snippets, many=True)
        return Response({"test":"data"})

    elif request.method == 'POST':
        datavalues1= request.data
        print(datavalues1)
        # serializer = SnippetSerializer(data=request.data)
        # if serializer.is_valid():
        return Response(datavalues1, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# create a viewset
class GeeksViewSet(viewsets.ModelViewSet):
	# define queryset
	queryset = GeeksModel.objects.all()
	
	# specify serializer to be used
	serializer_class = GeeksSerializer


from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *

# Create your views here.



   
  
# Imports PIL module 
from PIL import Image as im


def hotel_image_view(request):
    if request.method == 'GET':
        return HttpResponse("GEt done")
    if request.method == 'POST':
            form = HotelForm(request.POST, request.FILES)
            test_data =dict(request.FILES)

            # print(type(request.FILES))
            # print(type(test_data.get('image')[0]))

            img = im.open(test_data.get('image')[0])
            predicted_value =predict(test_data.get('image')[0])
            print(img.save("yoloapi/media/images/test.jpg")) 

            if form.is_valid():
                    form.save()
            # return redirect('success')
            return HttpResponse(predicted_value)



	# else:
	# 	form = HotelForm()
	# return render(request, 'hotel_image_form.html', {'form': form})


from django.shortcuts import render
from .models import Hotel as Image

# Create your views here.
def index(request):
    data = Image.objects.all()
    context = {
        'data' : data
    }
    return render(request,"display.html", context)

def success(request):
	return HttpResponse('successfully uploaded')
