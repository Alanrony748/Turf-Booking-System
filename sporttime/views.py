from django.shortcuts import render,get_object_or_404
from sporttime.models import TurfDb,BookingDb
from sporttime.serializers import Turf_serializer,Booking_serializer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class TurfListView(APIView):
    def get(self,request):
        qs=TurfDb.objects.all()
        serializer_instance=Turf_serializer(qs,many=True)
        return Response(data=serializer_instance.data)


    def post(self,request):
        form_data=request.data
        serializer_instance=Turf_serializer(data=form_data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)


class TurfRetreiveUpdateDelete(APIView):
    def get(self,request,pk):
        qs=get_object_or_404(TurfDb,id=pk)
        serializer_instance=Turf_serializer(qs)
        return Response(data=serializer_instance.data)

    def put(self,request,pk):
        form_data=request.data
        Turf_object=get_object_or_404(TurfDb,id=pk)
        serializer_instance=Turf_serializer(data=form_data,instance=Turf_object)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

    def delete(self,request,pk):
        turf_object=get_object_or_404(TurfDb,id=pk)
        turf_object.delete()
        return Response(data={
            "message":"deleted successfully"
        })


class BookingListView(APIView):
    def get(self,request):
        qs=BookingDb.objects.all()
        serializer_instance=Booking_serializer(qs,many=True)
        return Response(data=serializer_instance.data)

    def post(self,request):
        form_data=request.data
        serializer_instance=Booking_serializer(data=form_data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data={
                "message":"Booking Successful"
            })
        else:
            return Response(data=serializer_instance.errors)




