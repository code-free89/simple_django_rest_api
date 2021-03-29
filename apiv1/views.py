from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, views
from .serializers import DataSerializer
import requests
import json

dummy_url = "https://dummy.restapiexample.com/api/v1/employees"
service2_url = "https://api.mocki.io/v1/b043df5a"
order_url = "https://dummy.restapiexample.com/api/v1/create"

class data(views.APIView):

    # Get all data
    def get(self, request):
        print("backend processing ...")
        headers = {
           'Content-Type': 'application/json',
           'Accept': 'text/plain',
           'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0'
        }
        result = requests.get(dummy_url, headers=headers)
        print("backend processing 1 ...", result.text)

        results = json.loads(result.text)

        # results = DataSerializer(result.content, many=True).data
        print("backend processing 2 ...", results)

        return Response(results)

class Orders(views.APIView):

    # Get all data
    def post(self, request):
        print("backend processing ...")
        data = {
            "name": "test",
            "salary": "123",
            "age": "23"
        }
        headers = {
           'Content-Type': 'application/json',
           'Accept': 'text/plain',
           'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0'
        }
        response = requests.request("POST", order_url, headers=headers, data=data)
        print("backend processing 1 ...", response.text)

        results = json.loads(response.text)

        # # # results = DataSerializer(result.content, many=True).data
        # print("backend processing 2 ...", results)

        return Response(results)

class Service2(views.APIView):

    # Get all data
    def get(self, request):
        print("backend processing ...")
        headers = {
           'Content-Type': 'application/json',
           'Accept': 'text/plain',
           'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0'
        }
        result = requests.get(service2_url, headers=headers)
        print("backend processing 1 ...", result.text)

        results = json.loads(result.text)

        # results = DataSerializer(result.content, many=True).data
        print("backend processing 2 ...", results)

        return Response(results)