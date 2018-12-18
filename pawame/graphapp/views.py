from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from graphapp.serializers import GraphDataSerializer
from rest_framework.views import APIView
import random
from django.http import JsonResponse
import json
from asgiref.sync import async_to_sync

# Create your views here.

class GraphDataView(APIView):

    def post(self, request):
        data = request.data
        serializer = GraphDataSerializer(data=data)

        if serializer.is_valid():
            # Use the data received to generate random numbers
            input1 = serializer.validated_data.get("inputRange1")
            input2 = serializer.validated_data.get("inputRange2")
            random_number = random.randint(input1, input2)
            data = {"status":1, "message":random_number}
            return Response(data, status=status.HTTP_200_OK)
            pass
        data = {"status": 0, "message": "The data is invalid"}
        return Response(data, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        message = {
            "inputRange1":1,
            "inputRange2":8
        }
        serializer = GraphDataSerializer(message)
        data = {"status":1, "message":serializer.data}
        async_to_sync(channel_layer.group_send)("chat", {"type": "chat.force_disconnect"})
        return Response(data, status.HTTP_200_OK)


    # def post(self,request):




# class PublisherView(View):
#
#     def post(self, request):
#         try:
#             key = request.META['HTTP_API_KEY']
#             if not key in settings.API_KEYS:
#                 return JsonResponse(
#                     {'error': 'API-KEY not valid'}, status=400)
#         except:
#             return JsonResponse(
#                 {'error': 'API-KEY missing in headers'}, status=400)
#         try:
#             body = json.loads(request.body.decode('utf-8'))
#         except:
#             return JsonResponse(
#                 {'error': 'POST data is not JSON'}, status=400)
#         try:
#             group = body['network']
#         except:
#             return JsonResponse(
#                 {'error': '*network* key missing'}, status=400)
#         if group not in settings.API_KEYS[key]:
#             return JsonResponse(
#                 {'error': 'You cannot broadcast to this channel'}, status=403)
#         if not 'data' in body:
#             return JsonResponse(
#                 {'error': '*data* key missing'}, status=400)
#         if not isinstance(body['data'], dict):
#             return JsonResponse(
#                 {'error': 'Can only broadcast json data'}, status=400)
#         # all tests are OK
#         Group(group).send({'text': json.dumps(body['data'])})
#         return JsonResponse({'message': 'OK'}, status=200)