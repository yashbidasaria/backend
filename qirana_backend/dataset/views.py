# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from qirana_backend.dataset.models import dataset_meta, dblp_meta, crash_meta, world_city_meta, world_country_meta, world_countryLang_meta, ssb_dwdate, ssb_customer, ssb_supplier, ssb_part, ssb_lineorder, tpch_customer, tpch_nation, tpch_lineitem
from qirana_backend.dataset.serializers import nameSerializer, dblpSerializer, crashSerializer, worldCitySerializer, worldCountrySerializer, worldLangSerializer, ssb_customerSer, ssb_dwdateSer, ssb_partSer, ssb_supSer, ssb_lineSer, tpch_NationSer, tpch_CustSer
# Create your views here.
def list(request):
    if request.method == 'GET':
        try:
            data = json.loads(open('C:/Users/Yashbidasaria/Desktop/datasets.json').read())
        except 'FileNotFoundError':
            print("Error in reading file")
        #data = data.replace('\n', ''),
        #data = data.replace('\t', '')
        #data = data.replace("\"", '')

        jsonData = json.dumps(data)
        datasets = dataset_meta.objects.all()
        serializer = nameSerializer(datasets, many=True)
        # return Response(serializer.data)
        return JsonResponse(data, safe=False)

def dblp_data(request):
    if request.method == 'GET':
        data = dblp_meta.objects.all()[:5]
        serializer = dblpSerializer(data, many=True)
        # return Response(serializer.data)
        return JsonResponse(serializer.data, safe=False)

def crash_data(request):
    if request.method == 'GET':
        data = crash_meta.objects.all()[:5]
        serializer = crashSerializer(data, many=True)
        # return Response(serializer.data)
        return JsonResponse(serializer.data, safe=False)

def worldCity_data(request):
    if request.method == 'GET':
        data = world_city_meta.objects.all()[:5]
        serializer = worldCitySerializer(data, many=True)
        # return Response(serializer.data)
        return JsonResponse(serializer.data, safe=False)

def worldCountry_data(request):
    if request.method == 'GET':
        data = world_country_meta.objects.all()[:5]
        serializer = worldCountrySerializer(data, many=True)
        # return Response(serializer.data)
        return JsonResponse(serializer.data, safe=False)

def worldLang_data(request):
    if request.method == 'GET':
        data = world_countryLang_meta.objects.all()[:5]
        serializer = worldLangSerializer(data, many=True)
        # return Response(serializer.data)
        return JsonResponse(serializer.data, safe=False)

def ssbCust_data(request):
    if request.method == 'GET':
        data = ssb_customer.objects.all()[:5]
        serializer = ssb_customerSer(data, many=True)
        return JsonResponse(serializer.data, safe=False)

def ssbDwdate_data(request):
    if request.method == 'GET':
        data = ssb_dwdate.objects.all()[:5]
        serializer = ssb_dwdateSer(data, many=True)
        return JsonResponse(serializer.data, safe=False)

def ssbpart_data(request):
    if request.method == 'GET':
        data = ssb_part.objects.all()[:5]
        serializer = ssb_partSer(data, many=True)
        return JsonResponse(serializer.data, safe=False)

def ssbsup_data(request):
    if request.method == 'GET':
        data = ssb_supplier.objects.all()[:5]
        serializer = ssb_supSer(data, many=True)
        return JsonResponse(serializer.data, safe=False)

def ssbLine_data(request):
    if request.method == 'GET':
        data = ssb_lineorder.objects.all()[:5]
        serializer = ssb_lineSer(data, many=True)
        return JsonResponse(serializer.data, safe=False)

def tpchCust_data(request):
    if request.method == 'GET':
        data = tpch_customer.objects.all()[:5]
        serializer = tpch_CustSer(data, many=True)
        return JsonResponse(serializer.data, safe=False)

def tpchNation_data(request):
    if request.method == 'GET':
        data = tpch_nation.objects.all()[:5]
        serializer = tpch_NationSer(data, many=True)
        return JsonResponse(serializer.data, safe=False)

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'buyer_2.html', context=None)




