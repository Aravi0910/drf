from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import StudDetails, VoterId, CricketPlayers,Team
from .serializer import serialization, VotingPerson, Cricketer_list
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, mixins, generics
from rest_framework.views import APIView
from rest_framework import viewsets



@api_view(['GET'])
def stud_list(request,format=None):
    if request.method == "GET":
        stud = StudDetails.objects.all()
        serializer = serialization(stud, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def stud_get(request, pk):
    if request.method == "GET":
        stud = StudDetails.objects.get(id=pk)
        serialize = serialization(stud, many=False)
        return Response(serialize.data)
    
@api_view(['POST'])
def stud_create(request):    
    serial = serialization(data=request.data)

    if serial.is_valid():        
        serial.save()
    return Response(serial.data)

@api_view(['PUT'])
def stud_update(request, pk):
    stud = StudDetails.objects.get(id=pk)
    serializer = serialization(instance=stud, data=request.data)

    if serializer.is_valid():
        serializer.save()    
        return Response(serializer.data)

@api_view(['DELETE'])
def stud_delete(request, pk):
    stud = StudDetails.objects.get(id=pk) 
    stud.delete()
    return Response('data successfully deleted')

@api_view(['GET', 'PUT', 'DELETE'])
def stud_details(request, pk):

    try:
        stud = StudDetails.objects.get(id=pk)
    except StudDetails.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':        
        serialize = serialization(stud, many=False)
        return Response(serialize.data)
    
    elif request.method == 'PUT':
        stud = StudDetails.objects.get(id=pk)
        serializer = serialization(instance=stud, data=request.data)

        if serializer.is_valid():
            serializer.save()        
        return Response(serializer.data)

    elif request.ethod == "DELETE":
        stud = StudDetails.objects.get(id=pk) 
        stud.delete()
        return Response('data successfully deleted')

@api_view(['GET', 'POST'])
def student_cv(request):
    if request.method == 'GET':
        stud = StudDetails.objects.all()
        serializer = serialization(stud, many=True)      
        return Response(serializer.data)
    
    elif request.method == 'POST':
        # data = request.data
        serializer = serialization(data=request.data)
        
        if serializer.is_valid():            
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class StudentList(APIView):
    def get(self, request, format=None):
        stud = StudDetails.objects.all()
        serializer = serialization(stud, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = serialization(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Student(APIView):
    def get_object(self, pk):
        try:
            return StudDetails.objects.get(id=pk)
        except StudDetails.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def get(self, request, pk, format=None):
        stud = self.get_object(pk)
        serializer = serialization(stud)
        return Response(serializer.data)
    
    def put(self, request, pk, formet=None):
        stud = self.get_object(pk)
        serializer = serialization(stud, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        stud = self.get_object(pk)
        stud.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Mixins   
class StudMixinList(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    generics.GenericAPIView):
    queryset = StudDetails.objects.all()
    serializer_class = serialization

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwagrs):
        return self.create(request, *args, **kwagrs)
    
class StudMixinDetails(mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       generics.GenericAPIView):
    queryset = StudDetails.objects.all()
    serializer_class = serialization

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# Generic class-based views
class StudGenericList(generics.ListCreateAPIView):
    queryset = StudDetails.objects.all()
    serializer_class = serialization

class StudGenericDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudDetails.objects.all()
    serializer_class = serialization

class CricketerList(generics.ListCreateAPIView):
    queryset = CricketPlayers.objects.all()
    serializer_class = Cricketer_list

class CricketerView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CricketPlayers.objects.all()
    serializer_class = Cricketer_list
    

class VotingMixinList(mixins.ListModelMixin,

                    mixins.CreateModelMixin,
                    generics.GenericAPIView):
    queryset = VoterId.objects.all()
    serializer_class = VotingPerson

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwagrs):
        return self.create(request, *args, **kwagrs)
    
class CricketerFilters(APIView):
    def get(self, request, pk):
        team_name = Team.objects.get(pk=pk)
        find = team_name.team.all()
        serializer = Cricketer_list(find, many=True)
        return Response(serializer.data)
    
# viewsets
class CricketerViewsets(viewsets.ModelViewSet):
    queryset = CricketPlayers.objects.all()
    serializer_class = Cricketer_list
    