from rest_framework.response import Response
from rest_framework import status
from logistics_api.serializers import *
from .models import requesterData, riderData
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET', 'POST'])
def assetrequester(request):
    if request.method == 'GET':
        data = requesterData.objects.all()
        serializer = RequesterSerializer(data, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        print(request.data)
        serializer = RequesterSerializer(data=request.data)
        #print(serializer.is_valid())
        #serializer.save()
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            print(serializer.errors)


@api_view(['GET', 'POST'])
def retrieveRequester(request):
    if request.method == 'GET':
        # get requester ID
        requesterId = request.query_params['id']
        print(requesterId)
#        requesterId = request.GET.get(id)
        if requesterId:
            allObjects = requesterData.objects.filter(requesterId=requesterId).order_by('Date_n_Time')
            serializer = RequesterSerializer(allObjects, many=True)
            return Response(serializer.data)


@api_view(['POST'])
def riderTravelInfo(request):
    if request.method == 'POST':
        serializer = RiderSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            print(serializer.errors)

@api_view(['POST'])
def matchRequests(request):
    if request.method == 'POST':
        address_and_Date = request.data
        print(address_and_Date)
        allCorrectRequest = riderData.objects.filter(fromAddress=address_and_Date['fromAddress'], toAddress=address_and_Date['toAddress'], Date_n_Time=address_and_Date['Date_n_Time'])
        serializer = RiderSerializer(allCorrectRequest, many=True)
        return Response(serializer.data)


@api_view(['PATCH'])
def apply(request):
    if request.method == 'PATCH':
        print(request.user)
        id = request.data['id']
        print(id)
        objectList = riderData.objects.filter(riderId=id)
        print(objectList)
        #objectList[0].status = 'APPLIED'
        print(id)

        print(id)
        serializer = RiderSerializer(objectList, many=True)
        print(serializer)
        if serializer.is_valid():

            return Response(serializer.data)
        else:
            print(serializer.errors)