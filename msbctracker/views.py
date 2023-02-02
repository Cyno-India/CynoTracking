from ast import Not
import datetime
from itertools import tee
from optparse import TitledHelpFormatter
from re import A
from unicodedata import numeric
from urllib import request
from xxlimited import new
from django.shortcuts import render
from rest_framework import status
from django.core.paginator import Paginator
from rest_framework.parsers import MultiPartParser, FormParser
from .functions import numbers
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse
import json
from .models import *
from rest_framework.decorators import api_view
import requests
from django.views.decorators.csrf import csrf_exempt

from rest_framework.generics import ListAPIView
# from .pagintaion import MyPagination
# Create your views here.
from pytz import timezone 
from datetime import datetime
import pandas
from rest_framework import permissions, status

from rest_framework.pagination import PageNumberPagination
from . pagintaion import PaginationHandlerMixin




from urllib import request
from django.shortcuts import render, HttpResponse
from rest_framework.parsers import MultiPartParser, FormParser
import math
# Create your views here.

# Create your views here.
from logging import raiseExceptions
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View
# from matplotlib.style import available

from rest_framework.views import APIView

from .serializers import *
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
import json
from .models import *
from rest_framework. exceptions import AuthenticationFailed
from rest_framework import status
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated
import datetime
from rest_framework.authentication import BasicAuthentication
from datetime import date, datetime

from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser
from django.shortcuts import render
from django.http import HttpResponseRedirect

import re
from rest_framework import permissions, status


# @csrf_exempt
# @api_view(['POST'])
def track():
    # track = request.get('tracking_number')
    # print(track)
    # code = request.data['carrier_code']
    # print(code)
    print('hello')
    json =  {
        "tracking_number":"RD040924587IN",
        "carrier_code": "india-post"
    }
    api_url = "https://api.tracktry.com/v1/trackings/get?limit=2000"
    print("API HITTTTT")
    # headers =  {"Content-Type":"application/json","Tracktry-Api-Key":"27654af3-b244-4192-b7d8-ce32be8d86c4"}
    headers =  {"Content-Type":"application/json","Tracktry-Api-Key":"ae2e8060-296c-4423-a980-c9e166e51498"}

    # data = {
    # "tracking_number":t,
    # "carrier_code": "india-post"
    # }
    # data = t,c

    response = requests.get(api_url, headers=headers)
    print("RESPONSE HIT")
    print(response)
    print('hellooo')
    res = response.json()
    # temp = {
    #     "status":res['data'][0]['status'],
    #     "id":res['data'][0]['id']
    # }
    return res

# @csrf_exempt
# class track(APIView):
# @csrf_exempt
# def tracker(tracking_number, carrier_code):
#     url_endpoint = f'https://api.tracktry.com/v1/trackings/realtime?tracking_number={tracking_number}&carrier_code={carrier_code}'
#     headers =  {"Content-Type":"application/json","Tracktry-Api-Key":"27654af3-b244-4192-b7d8-ce32be8d86c4"}

#     response = requests.post(url_endpoint, headers=headers)
#     print('response')
#     # print(response)
#     # print(response.content)
#     # response = b'{"Status":"Success","Details":"95dc91bb-e6f4-4fcc-9163-eea370bcde14"}'
#     # return Response(response)

# # class track(APIView):
# @csrf_exempt
# @api_view(["POST"])
# def post(request):
#     track = request.data['tracking_number']
#     print(track)
#     code = request.data['carrier_code']
#     print(code)
#     url_endpoint = f'https://api.tracktry.com/v1/trackings/realtime?tracking_number={track}&carrier_code={code}'
#     headers =  {"Content-Type":"application/json","Tracktry-Api-Key":"27654af3-b244-4192-b7d8-ce32be8d86c4"}
#     res = requests.post(url_endpoint, headers=headers)

#     # t = tracker(tracking_number=track,carrier_code=code)
#     print(res)
#     return Response(res)

# def t():
#     urlStr ='https://api.tracktry.com/v1/trackings/realtime'
#     requestData ="{\"tracking_number\": \"RD040924587IN\",\"carrier_code\":\"india-post\"}"
#     result = requests.post(requestData, urlStr, "realtime")
#     print(result)

# t()


        

class GetTrackDetails(APIView):
    def get(self, request):
    #    t = Tracker.objects.all().values('id','api_call_time','status','tracking_number','updated_time','booked','arrival','outbound','delivered')
       t = Tracker.objects.all().delete()
       return Response("DONE")

# class GetDetails(APIView):
    # queryset = Tracker.objects.filter(status="Available").values('api_call_time','status','tracking_number','updated_time','booked','arrival','outbound','delivered')
    # # print(queryset,'dict')
    # serializer_class = TrackSerializer
    # pagination_class =MyPagination
    # queryset.update(atTU)

class BasicPagination(PageNumberPagination):
    page_size_query_param = 'limit'

class GetDetails(APIView, PaginationHandlerMixin):
    pagination_class = BasicPagination
    serializer_class = TrackDetailsSerializer
    def get(self, request, format=None, *args, **kwargs):
        instance = Tracker.objects.filter(status="Available").values('api_call_time','status','tracking_number','updated_time','booked','arrival','outbound','delivered')
        # print(instance)
        ind_time = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S.%f')
        page = self.paginate_queryset(instance)
        if page is not None:
            serializer = self.get_paginated_response(self.serializer_class(page, many=True).data)
            s = serializer.data['results']
            print(s)
            for i in s:
                l = i['tracking_number']
                print(l)
                Tracker.objects.filter(tracking_number=l).update(status="Delivered",numeric_status=5,api_call_time=ind_time)
        else:
            serializer = self.serializer_class(instance, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# class PatchDetails(APIView):

#     def patch(self,request, tracking_number=[]):
#         if tracking_number is not None:
#             for new_t in tracking_number:
#                 s = new_t
#                 print(s)
#             return Response('HEllo')

                    

class PatchDetails(ListAPIView):
    queryset = Tracker.objects.all()
    serializer_class = TrackDetailsSerializer
    # filterset_class = PackageFilter

 
    def get_queryset(self):
        track = self.request.query_params.get('tracking_numbers', None)
        numbers = []
        ind_time = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S.%f')
        try:
            if track is not None:
                for year in track.split('|'):
                    numbers.append(year)
            print(numbers)
            for n in numbers:
                print(n)
                # s = Tracker.objects.all().values('tracking_number')
                # if n.exists() in s:
                
                Tracker.objects.filter(tracking_number=n).update(status="shipped",msbc_patch_api_call_time=ind_time,numeric_status=3,api_call_time=ind_time)
                # print(s)
            return "DOne"

        except:
            pass
        # print(t,'tasdasdas')
        # tn = request.data['tracking_number']
        # print(tn,'asdasdasd')
        # T = Tracker.objects.filter(tracking_number=tn).update(status="Assigned")

        # return Response("Shipped")

class PostingTrack(APIView):
    # parser_classes = [parsers.MultiPartParser, parsers.FormParser]
    
    def post(self,request):
        if request.method == "POST":
                # print()
                allimages = request.FILES['file']
                print('fileeeeee',allimages)
                excel_data_df = pandas.read_excel(allimages, sheet_name='Sheet1')
                # print('HIIIIIIIIIIOOO',excel_data_df)
                tr = []
                for ind in excel_data_df.index:
                    p = excel_data_df['tracking_number\t'][ind]
                    track = {
                        "tracking_number":p,
                        "carrier_code":"india-post"
                    }  
                    tr.append(track) 
                print(tr)
                numbers(tr)
                # for i in tr:
                #     print(i)     
                # numbers(tr)
        return Response('DONE')

# def get_difference(list_a, list_b):
#     non_match_a  = set(list_a)-set(list_b)
#     non_match_b  = set(list_b)-set(list_a)
#     non_match = list(non_match_a) + list(non_match_b)
#     print(non_match)

class GetTrackingDetails(APIView):
    def get(self, request):
        request_data = request.data
        # t = request_data['tracking_number']
        # print(track)
        te = track()
        # print(te['data']['items'][0]['status'],'ttttttt')
        new_dict=  te['data']['items']
        print(len(new_dict))
        # x = new_dict['destination_info']['trackinfo']
        # print(x)
        new_temp = []
        # try:
        for i in new_dict:
            status = i['status']
            tracking_number = i['tracking_number']
            updated_time = i['updated_at']
            tracking_info = i['destination_info']['trackinfo']
            origin_info = i['origin_info']['trackinfo']
            last_event = i['lastEvent']
            if tracking_info is None:
                # print(tracking_number,'ORIGIN INFO TRACK')
                booked = ""
                outbound_date= ""
                arrival_date= ""
                delivered_date= ""
                tracking_info = ""
                new_status = ""
                if origin_info:
                    for new_t in origin_info:
                        date = new_t['Date']
                        status_desc = new_t['StatusDescription']
                        details = new_t['Details']
                        # print('OROGINNN DATE AND STATUS',tracking_number,date,status_desc)
                        if "Booked" in status_desc or "Booked,Air" in status_desc: 
                                ## Changed to CONTAINS
                            # print('STATUSS DESC',tracking_number,status_desc)
                            booked = date
                        # else:
                        #     if "Item Booked,Air" in status_desc:
                        #         print('STATUSS DESC',status_desc)
                                # booked = date
                        if "Item Received" in status_desc and "KAWASAKI" in details:
                            arrival_date = date

                        if "(Otb)" in status_desc:
                            outbound_date = date
                        else:
                            if "Bagged,Air" in status_desc:
                                outbound_date = date

                        if "Delivery Confirmed" in status_desc:
                            delivered_date = date

                           
                        if "TOKYO INT BAG" in details:
                            # print('ORIGIN DETAAILLSSS',tracking_number,details,status_desc)
                            new_status = "Returned"                     

                json = {
                    "new_status":new_status,
                    "tracking":tracking_number,
                    "booked":booked,
                    "outbound":outbound_date,
                    "arrival":arrival_date,
                    "delivered":delivered_date,
                },
                # print(json)

                
            elif tracking_info is not None:
                booked = ""
                outbound_date= ""
                arrival_date= ""
                delivered_date= ""
                new_status = ""
                for t in tracking_info:
                    date = t['Date']
                    status_desc = t['StatusDescription']
                    details = t['Details']
                    if "Posting/Collection " in status_desc:
                        booked = date
                    # if booked == "":
                    #     for new_t in origin_info:
                    #         date = new_t['Date']
                    #         status_desc = new_t['StatusDescription']
                    #         # print('OROGINNN DATE AND STATUS',date,status_desc)
                    #         if status_desc == "Item Bagged":
                    #             print('STATUSS DESC',status_desc,date)
                    #             booked = date
                    if "Dispatch from outward office of exchange " in status_desc:
                        outbound_date = date
                    if "Arrival at inward office of exchange " in status_desc:
                        arrival_date = date
                    if "Final delivery " in status_desc:
                        delivered_date = date
                
                if booked == "":
                    # print('EMPTYYY BOOKED',booked)
                    for j in origin_info:
                        date = j['Date']
                        status_desc = j['StatusDescription']
                        # print('ORIGN BOOK',status_desc)
                        if "Booked,Air" in status_desc:
                            # print('STATUSS DESC',status_desc,date)
                            booked = date
                # if outbound_date == "":
                #     print('EMPTYYY BOOKED',outbound_date)
                #     for p in origin_info:
                #         date = p['Date']
                #         status_desc = p['StatusDescription']
                #         # print('ORIGN BOOK',status_desc)
                #         if "Bagged,Air" in status_desc:
                #             print('STATUSS DESC',tracking_number,status_desc,date)
                #             outbound_date = date
        
                    # if "TOKYO INT BAG" in details:
                    #     print('ORIGIN DETAAILLSSS',tracking_number,details,status_desc)
                    #     new_status = "Returned"  
                    # if "TOKYO" in details:
                    #     print('DETAAILLSSS',details)          
                    
                
                json2 = {
                    "new_Status":new_status,
                    "tracking":tracking_number,
                    "booked":booked,
                    "outbound":outbound_date,
                    "arrival":arrival_date,
                    "delivered":delivered_date,
                },
                # print(json2)
            if new_status:              ####   Staus handling if booked and item delivery is confirmed
                status = "Returned"
            else :
                if status == "delivered":              ####   Staus handling if booked and item delivery is confirmed
                    status = "Delivered"
                else:
                    if delivered_date:
                        status = "Delivered"
                    elif arrival_date:
                        status = "Arrival"
                    elif outbound_date:
                        status = "OutBound"
                    elif booked:
                        status = "Booked"
                    elif new_status:
                        status = "Returned"
                # print(booked,'ORIGN BOOK')
            # if booked == "":
            #     print('1',booked)
            #     for new_t in origin_info:
            #         print("PPPPPP")
            #         date = new_t['Date']
            #         status_desc = new_t['StatusDescription']
            #         print('ORIGN BOOK',status_desc)
            #         if "Booked" in status_desc:
            #             print('STATUSS DESC',status_desc,date)
                            # booked = date
                            # print('ORIGN BOOK',booked)
                            # booked = dateß
                            # print('CHAL GYA BHAI')
                                

            d = {
                "status": status,
                "tracking_number":tracking_number,
                "updated_time":updated_time,    
                "Booked":booked,
                "OutBound":outbound_date,
                "Arrival":arrival_date,
                "Delivered":delivered_date,
                "lastEvent":last_event,
                # "origin_info":origin_info,
                "tracking_info":tracking_info

            }
            new_temp.append(d)

        

        for new in new_temp:
            s = new['status']
            if s == "notfound":
                s = "Available"
            # if s == "expired":
            #     Tracker.objects.update(bad=True)
            t = new['tracking_number']
            u =new['updated_time']
            b = new['Booked']
            a = new['Arrival']
            d = new['Delivered']
            o = new['OutBound']
            i = new['tracking_info']
            if d:
                s = "Delivered"
            elif o:
                s = "Outbound"
            elif a:
                s = "Arrived"
            elif b:
                s = "Booked"
            
            # print(s)

            # if b is None:
            #     pass
            # else:
            #     s = "Booked"
            #     break
            

            # if a is None:
            #     pass
            # else:
            #     s = "Arrived"
            #     break


            # if o is None:
            #     pass
            # else:
            #     s = "Outbound"
            #     break
            


            
            

            ind_time = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S.%f')
            # print('REEEACHED HEREEEEE GETDETAILS')
        #     for new_t in new_dict:
        #           tracking_number = new_t['tracking_number']
        #           Tracker.objects.filter(tracking_number=new_t).update(api_call_time=ind_time,status=s,updated_time=u,booked=b,arrival=a,outbound=o,delivered=d,tracking_info=i

        
        
        # )




            # print(current_time)


            if s == "Available":
                ns = "0"
            if s == "transit":
                ns = "1"                    
            elif s == "hold":
                ns = "2"
            elif s == "shipped":
                ns = "3"
            elif s =="expired":
                ns = "4"
            elif s == "Booked":
                ns = "5"
            elif s == "Outbound":
                ns = "6"
            elif s == "Arrived":
                ns = "7"
            elif s == "Delivered":
                ns = "8"
            
            # print('NSSSSS',ns)
#                 new_data = Tracker.objects.create(api_call_time=ind_time,status=s,tracking_number=t,updated_time=u,booked=b,arrival=a,outbound=o,delivered=d,tracking_info=i,numeric_status=ns
            
#         )


            # new_data = Tracker.objects.create(api_call_time=ind_time,status=s,tracking_number=t,updated_time=u,booked=b,arrival=a,outbound=o,delivered=d,tracking_info=i,numeric_status=ns
        
    # )

    # except:
    #     pass    
    # ttt = Tracker.objects.all().values()
    # print('tttttt',ttt)
        # return Response('Error')
        # print(new_dict)
        return Response(new_temp)
    
    def patch(self, request):
        request_data = request.data
        # t = request_data['tracking_number']
        # print(track)
        te = track()
        # print(te['data']['items'][0]['status'],'ttttttt')
        new_dict=  te['data']['items']
        print(len(new_dict))
        # x = new_dict['destination_info']['trackinfo']
        # print(x)
        new_temp = []
        try:
            for i in new_dict:
                status = i['status']
                tracking_number = i['tracking_number']
                updated_time = i['updated_at']
                print('TRRRACK',tracking_number)
                tracking_info = i['destination_info']['trackinfo']
                origin_info = i['origin_info']['trackinfo']
                last_event = i['lastEvent']
                if tracking_info is None:
                    booked = ""
                    if origin_info:
                        for new_t in origin_info:
                            date = new_t['Date']
                            status_desc = new_t['StatusDescription']
                            # print('OROGINNN DATE AND STATUS',date,status_desc)
                            if status_desc ==  "Item Booked":
                                print('STATUSS DESC',status_desc,date)
                                booked = date
                    arrival_date= ""
                    outbound_date= ""
                    delivered_date= ""
                    tracking_info = ""

                    
                elif tracking_info is not None:
                    booked = ""
                    arrival_date= ""
                    outbound_date= ""
                    delivered_date= ""

                    for t in tracking_info:
                        date = t['Date']
                        status_desc = t['StatusDescription']

                        if status_desc == "Posting/Collection ":
                            booked = date
                        if status_desc == "Dispatch from outward office of exchange ":
                            outbound_date = date
                        if status_desc == "Arrival at inward office of exchange ":
                            arrival_date = date
                        if status_desc == "Final delivery ":
                            delivered_date = date
                        if booked:
                            status = "Booked"
                        if arrival_date:
                            status = "Arrival"
                        if outbound_date:
                            status = "OutBound"
                        if delivered_date:
                            status = "Delivered"

                        
                    # if booked == "":
                    #     for new_t in origin_info:
                    #         date = new_t['Date']
                    #         status_desc = new_t['StatusDescription']
                    #         # print('OROGINNN DATE AND STATUS',date,status_desc)
                    #         if status_desc ==  "Item Booked":
                    #             print('STATUSS DESC',status_desc,date)
                    #             booked = date

                d = {
                    "status": status,
                    "tracking_number":tracking_number,
                    "updated_time":updated_time,    
                    "Booked":booked,
                    "Arrival":arrival_date,
                    "OutBound":outbound_date,
                    "Delivered":delivered_date,
                    "lastEvent":last_event,
                    "tracking_info":tracking_info

                }
                new_temp.append(d)
            

            for new in new_temp:
                s = new['status']
                if s == "notfound":
                    s = "Available"

                # if s == "notfound":
                #     Tracker.objects.update(ready=True)
                # if s == "expired":
                #     Tracker.objects.update(bad=True)
                t = new['tracking_number']
                u =new['updated_time']
                b = new['Booked']
                a = new['Arrival']
                d = new['Delivered']
                o = new['OutBound']
                i = new['tracking_info']
                if d:
                    s = "Delivered"
                elif o:
                    s = "Outbound"
                elif a:
                    s = "Arrived"
                elif b:
                    s = "Booked"
                
                # hold_status = Tracker.objects.filter(tracking_number=t).values_list('status')[0][0]
                # print('HOLLDDDDDD STATUS',hold_status)
                # numeric_status = Tracker.objects.filter(tracking_number=t).values_list('numeric_status')[0][0]

                # # print(hold_status,'holdstatus')
                # if s == "notfound" and hold_status == "hold":
                #     s = "hold"
                # elif s == "Available" and hold_status == "shipped":
                #     s = "shipped"
                # for h in hold_status:
                #     if hold_status == "hold":
                ind_time = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S.%f')
                if s == "Available":
                    ns = "0"
                if s == "transit":
                    ns = "1"                    
                elif s == "hold":
                    ns = "2"
                elif s == "shipped":
                    ns = "3"
                elif s =="expired":
                    ns = "4"
                elif s == "Booked":
                    ns = "5"
                elif s == "Outbound":
                    ns = "6"
                elif s == "Arrived":
                    ns = "7"
                elif s == "Delivered":
                    ns = "8"
                
                # print('NSSSSS',ns)
                # if s == "Available" and numeric_status < 1 or s == "hold" and numeric_status < 2  or s == "shipped" and numeric_status < 3 or s == "expired" and numeric_status < 4 or s == "Booked" and numeric_status < 5 or s == "Outbound" and numeric_status < 6 or s == "Arrived" and numeric_status < 7 or s == "Delivered" and numeric_status < 8:
                #     print('HELLLLLO')
                #     return Response('FAIILED')
            
                # for dm in s:
                #     s == "Assigned"
                #     Tracker.objects.filter(tracking_number=t).update(status=s)
            
                


                del_data = Tracker.objects.filter(tracking_number=t,status__in=["Available","Delivered","transit","Outbound","Booked","Arrived","expired","shipped"]).update(api_call_time=ind_time,status=s,updated_time=u,booked=b,arrival=a,outbound=o,delivered=d,tracking_info=i,numeric_status=ns)
                

                # if b is None:
                #     pass
                # else:
                #     s = "Booked"
                #     break
                

                # if a is None:
                #     pass
                # else:
                #     s = "Arrived"
                #     break


                # if o is None:
                #     pass
                # else:
                #     s = "Outbound"
                #     break
                


                
                

                # ind_time = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S.%f')
                # for l in new_temp:
                #     tra = l['tracking_number']
                #     print(tra,'trackkkkky')
                #     del_data = Tracker.objects.filter(tracking_number=tra).update(api_call_time=ind_time,status=s,updated_time=u,booked=b,arrival=a,outbound=o,delivered=d,tracking_info=i)

                # Tracker.objects.filter(tracking_number=tracking_number).update(api_call_time=ind_time,status=s,updated_time=u,booked=b,arrival=a,outbound=o,delivered=d,tracking_info=i)

    


                # print(current_time)


            

            #     new_data = Tracker.objects.create(api_call_time=ind_time,status=s,tracking_number=t,updated_time=u,booked=b,arrival=a,outbound=o,delivered=d,tracking_info=i
            
            
        except:
            pass
            # )
                # return Response('Error')
                # print(new_dict)
        return Response(new_temp)

def create():
    # t = request_data['tracking_number']
    # print(track)
    te = track()
        # print(te['data']['items'][0]['status'],'ttttttt')
    new_dict=  te['data']['items']
    print(len(new_dict))
    # x = new_dict['destination_info']['trackinfo']
    # print(x)
    new_temp = []
    for i in new_dict:
        status = i['status']
        tracking_number = i['tracking_number']
        updated_time = i['updated_at']
        tracking_info = i['destination_info']['trackinfo']
        origin_info = i['origin_info']['trackinfo']
        # print('ORIGINNNN DATA',origin_info)
        last_event = i['lastEvent']
        if tracking_info is None:
            booked = ""
            if origin_info:
                for new_t in origin_info:
                        date = new_t['Date']
                        status_desc = new_t['StatusDescription']
                        # print('OROGINNN DATE AND STATUS',date,status_desc)
                        if status_desc ==  "Item Booked":
                            print('STATUSS DESC',status_desc,date)
                            booked = date
            arrival_date= ""
            outbound_date= ""
            delivered_date= ""
            tracking_info = ""

            
        elif tracking_info is not None:
            booked = ""
            arrival_date= ""
            outbound_date= ""
            delivered_date= ""

            for t in tracking_info:
                date = t['Date']
                status_desc = t['StatusDescription']
                
                if status_desc == "Posting/Collection ":
                    booked = date
                # if booked == "":
                #     for new_t in origin_info:
                #         date = new_t['Date']
                #         status_desc = new_t['StatusDescription']
                #         # print('OROGINNN DATE AND STATUS',date,status_desc)
                #         if status_desc == "Item Bagged":
                #             print('STATUSS DESC',status_desc,date)
                #             booked = date
                if status_desc == "Dispatch from outward office of exchange ":
                    outbound_date = date
                if status_desc == "Arrival at inward office of exchange ":
                    arrival_date = date
                if status_desc == "Final delivery ":
                    delivered_date = date
            
            # print(booked,'ORIGN BOOK')
            if booked == "":
                for new_t in origin_info:
                    date = new_t['Date']
                    status_desc = new_t['StatusDescription']
                    # print('OROGINNN DATE AND STATUS',date,status_desc)
                    if status_desc ==  "Item Booked":
                        print('STATUSS DESC',status_desc,date)
                        booked = date
                        # print('ORIGN BOOK',booked)
                    # booked = dateß
                    # print('CHAL GYA BHAI')
                    

        d = {
            "status": status,
            "tracking_number":tracking_number,
            "updated_time":updated_time,    
            "Booked":booked,
            "Arrival":arrival_date,
            "OutBound":outbound_date,
            "Delivered":delivered_date,
            "lastEvent":last_event,
            "tracking_info":tracking_info

        }
        new_temp.append(d)
    

    for new in new_temp:
        s = new['status']
        if s == "notfound":
            s = "Available"
        # if s == "expired":
        #     Tracker.objects.update(bad=True)
        t = new['tracking_number']
        u =new['updated_time']
        b = new['Booked']
        a = new['Arrival']
        d = new['Delivered']
        o = new['OutBound']
        i = new['tracking_info']
        if d:
            s = "Delivered"
        elif o:
            s = "Outbound"
        elif a:
            s = "Arrived"
        elif b:
            s = "Booked"
        
        print(s)

        # if b is None:
        #     pass
        # else:
        #     s = "Booked"
        #     break
        

        # if a is None:
        #     pass
        # else:
        #     s = "Arrived"
        #     break


        # if o is None:
        #     pass
        # else:
        #     s = "Outbound"
        #     break
        


        
        

        ind_time = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S.%f')
        print('REEEACHED HEREEEEE GETDETAILS')
    #     for new_t in new_dict:
    #           tracking_number = new_t['tracking_number']
    #           Tracker.objects.filter(tracking_number=new_t).update(api_call_time=ind_time,status=s,updated_time=u,booked=b,arrival=a,outbound=o,delivered=d,tracking_info=i

    
    
    # )



        # print(current_time)


        if s == "Available":
            ns = "0"
        if s == "transit":
            ns = "1"                    
        elif s == "hold":
            ns = "2"
        elif s == "shipped":
            ns = "3"
        elif s =="expired":
            ns = "4"
        elif s == "Booked":
            ns = "5"
        elif s == "Outbound":
            ns = "6"
        elif s == "Arrived":
            ns = "7"
        elif s == "Delivered":
            ns = "8"
        
        print('NSSSSS',ns)


        # new_data = Tracker.objects.create(api_call_time=ind_time,status=s,tracking_number=t,updated_time=u,booked=b,arrival=a,outbound=o,delivered=d,tracking_info=i,numeric_status=ns
    
# )

# except:
#     pass    
# ttt = Tracker.objects.all().values()
# print('tttttt',ttt)
    # return Response('Error')
    # print(new_dict)
    print('hiiii')

# create()

def update():
    # t = request_data['tracking_number']
    # print(track)
    te = track()
    # print(te['data']['items'][0]['status'],'ttttttt')
    new_dict=  te['data']['items']
    print(len(new_dict))
    # x = new_dict['destination_info']['trackinfo']
    # print(x)
    new_temp = []
    # del_data = Tracker.objects.all()
    # del_data.delete()
    try:
        for i in new_dict:
            status = i['status']
            tracking_number = i['tracking_number']
            updated_time = i['updated_at']
            tracking_info = i['destination_info']['trackinfo']
            if tracking_info is None:
                booked = ""
                arrival_date= ""
                outbound_date= ""
                delivered_date= ""
                tracking_info = ""

                
            elif tracking_info is not None:
                booked = ""
                arrival_date= ""
                outbound_date= ""
                delivered_date= ""

                for t in tracking_info:
                    date = t['Date']
                    status_desc = t['StatusDescription']

                    if status_desc == "Posting/Collection ":
                        booked = date
                    if status_desc == "Dispatch from outward office of exchange ":
                        outbound_date = date
                    if status_desc == "Arrival at inward office of exchange ":
                        arrival_date = date
                    if status_desc == "Final delivery ":
                        delivered_date = date

            d = {
                "status": status,
                "tracking_number":tracking_number,
                "updated_time":updated_time,
                "Booked":booked,
                "Arrival":arrival_date,
                "OutBound":outbound_date,
                "Delivered":delivered_date,
                "tracking_info":tracking_info

            }
            new_temp.append(d)

        for new in new_temp:
            s = new['status']
            if s == "notfound":
                s = "Available"
            # elif s == "expired":
            #     print('helllllooo')
            #     Tracker.objects.update(bad=True,ready=False, assigned=False)  
            # print('hiiiiiiiii')
            
            t = new['tracking_number']
            u =new['updated_time']
            b = new['Booked']
            a = new['Arrival']
            d = new['Delivered']
            o = new['OutBound']
            i = new['tracking_info']

            if d:
                s = "Delivered"
            elif o:
                s = "Outbound"
            elif a:
                s = "Arrived"
            elif b:
                s = "Booked"
            

            # if b is None:
            #     pass
            # else:
            #     s = "Booked"
            #     break
            

            # if a is None:
            #     pass
            # else:
            #     s = "Arrived"
            #     break


            # if o is None:
            #     pass
            # else:
            #     s = "Outbound"
            #     break
            


            
            



            # current_time = datetime.datetime.now()
            ind_time = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S.%f')
            for new_t in new_dict:
                  tracking = new_t['tracking_number']
                  Tracker.objects.filter(tracking_number=tracking).update(api_call_time=ind_time,status=s,updated_time=u,booked=b,arrival=a,outbound=o,delivered=d,tracking_info=i

        
        
        )


        #     new_data = Tracker.objects.create(api_call_time=ind_time,status=s,tracking_number=t,updated_time=u,booked=b,arrival=a,outbound=o,delivered=d,tracking_info=i

        
        
        # )
    except:
        pass
# print(new_dict)
    return new_temp



def createfunc():
    # request_data = requests.data
    # t = request_data['tracking_number']
    # print(track)
    te = track()
    # print(te['data']['items'][0]['status'],'ttttttt')
    new_dict=  te['data']['items']
    print(len(new_dict))
    # x = new_dict['destination_info']['trackinfo']
    # print(x)
    new_temp = []
    try:
        for i in new_dict:
            status = i['status']
            tracking_number = i['tracking_number']
            updated_time = i['updated_at']
            tracking_info = i['destination_info']['trackinfo']
            origin_info = i['origin_info']['trackinfo']
            last_event = i['lastEvent']
            if tracking_info is None:
                # print(tracking_number,'ORIGIN INFO TRACK')
                booked = ""
                outbound_date= ""
                arrival_date= ""
                delivered_date= ""
                tracking_info = ""
                new_status = ""
                if origin_info:
                    for new_t in origin_info:
                        date = new_t['Date']
                        status_desc = new_t['StatusDescription']
                        details = new_t['Details']
                        # print('OROGINNN DATE AND STATUS',tracking_number,date,status_desc)
                        if "Booked" in status_desc or "Booked,Air" in status_desc: 
                                ## Changed to CONTAINS
                            # print('STATUSS DESC',tracking_number,status_desc)
                            booked = date
                        # else:
                        #     if "Item Booked,Air" in status_desc:
                        #         print('STATUSS DESC',status_desc)
                                # booked = date
                        if "Item Received" in status_desc and "KAWASAKI" in details:
                            arrival_date = date

                        if "(Otb)" in status_desc:
                            outbound_date = date

                        if "Delivery Confirmed" in status_desc:
                            delivered_date = date

                            
                        if "TOKYO INT BAG" in details:
                            # print('ORIGIN DETAAILLSSS',tracking_number,details,status_desc)
                            new_status = "Returned"                     

                json = {
                    "new_status":new_status,
                    "tracking":tracking_number,
                    "booked":booked,
                    "outbound":outbound_date,
                    "arrival":arrival_date,
                    "delivered":delivered_date,
                },
                # print(json)

                
            elif tracking_info is not None:
                booked = ""
                outbound_date= ""
                arrival_date= ""
                delivered_date= ""
                new_status = ""
                for t in tracking_info:
                    date = t['Date']
                    status_desc = t['StatusDescription']
                    details = t['Details']
                    if "Posting/Collection " in status_desc:
                        booked = date
                    # if booked == "":
                    #     for new_t in origin_info:
                    #         date = new_t['Date']
                    #         status_desc = new_t['StatusDescription']
                    #         # print('OROGINNN DATE AND STATUS',date,status_desc)
                    #         if status_desc == "Item Bagged":
                    #             print('STATUSS DESC',status_desc,date)
                    #             booked = date
                    if "Dispatch from outward office of exchange " in status_desc:
                        outbound_date = date
                    if "Arrival at inward office of exchange " in status_desc:
                        arrival_date = date
                    if "Final delivery " in status_desc:
                        delivered_date = date
                
                if booked == "":
                    # print('EMPTYYY BOOKED',booked)
                    for j in origin_info:
                        date = j['Date']
                        status_desc = j['StatusDescription']
                        # print('ORIGN BOOK',status_desc)
                        if "Booked,Air" in status_desc:
                            print('STATUSS DESC',status_desc,date)
                            booked = date

                    # if "TOKYO INT BAG" in details:
                    #     print('ORIGIN DETAAILLSSS',tracking_number,details,status_desc)
                    #     new_status = "Returned"  
                    # if "TOKYO" in details:
                    #     print('DETAAILLSSS',details)          
                    
                
                json2 = {
                    "new_Status":new_status,
                    "tracking":tracking_number,
                    "booked":booked,
                    "outbound":outbound_date,
                    "arrival":arrival_date,
                    "delivered":delivered_date,
                },
                # print(json2)
            if new_status:              ####   Staus handling if booked and item delivery is confirmed
                status = "Returned"
            else :
                if status == "delivered":              ####   Staus handling if booked and item delivery is confirmed
                    status = "Delivered"
                else:
                    if delivered_date:
                        status = "Delivered"
                    elif arrival_date:
                        status = "Arrival"
                    elif outbound_date:
                        status = "OutBound"
                    elif booked:
                        status = "Booked"
                    elif new_status:
                        status = "Returned"
                # print(booked,'ORIGN BOOK')
            # if booked == "":
            #     print('1',booked)
            #     for new_t in origin_info:
            #         print("PPPPPP")
            #         date = new_t['Date']
            #         status_desc = new_t['StatusDescription']
            #         print('ORIGN BOOK',status_desc)
            #         if "Booked" in status_desc:
            #             print('STATUSS DESC',status_desc,date)
                            # booked = date
                            # print('ORIGN BOOK',booked)
                            # booked = dateß
                            # print('CHAL GYA BHAI')
                                

            d = {
                "status": status,
                "tracking_number":tracking_number,
                "updated_time":updated_time,    
                "Booked":booked,
                "OutBound":outbound_date,
                "Arrival":arrival_date,
                "Delivered":delivered_date,
                "lastEvent":last_event,
                # "origin_info":origin_info,
                "tracking_info":tracking_info

            }
            new_temp.append(d)

        

        for new in new_temp:
            s = new['status']
            if s == "notfound":
                s = "Available"
            # if s == "expired":
            #     Tracker.objects.update(bad=True)
            t = new['tracking_number']
            u =new['updated_time']
            b = new['Booked']
            a = new['Arrival']
            d = new['Delivered']
            o = new['OutBound']
            i = new['tracking_info']
            if d:
                s = "Delivered"
            elif o:
                s = "Outbound"
            elif a:
                s = "Arrived"
            elif b:
                s = "Booked"
            
            # print(s)

            # if b is None:
            #     pass
            # else:
            #     s = "Booked"
            #     break
            

            # if a is None:
            #     pass
            # else:
            #     s = "Arrived"
            #     break


            # if o is None:
            #     pass
            # else:
            #     s = "Outbound"
            #     break
            


            
            

            ind_time = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S.%f')
            # print('REEEACHED HEREEEEE GETDETAILS')
        #     for new_t in new_dict:
        #           tracking_number = new_t['tracking_number']
        #           Tracker.objects.filter(tracking_number=new_t).update(api_call_time=ind_time,status=s,updated_time=u,booked=b,arrival=a,outbound=o,delivered=d,tracking_info=i

        
        
        # )




            # print(current_time)


            if s == "Available":
                ns = "0"
            if s == "transit":
                ns = "1"                    
            elif s == "hold":
                ns = "2"
            elif s == "shipped":
                ns = "3"
            elif s =="expired":
                ns = "4"
            elif s == "Booked":
                ns = "5"
            elif s == "Outbound":
                ns = "6"
            elif s == "Arrived":
                ns = "7"
            elif s == "Delivered":
                ns = "8"
            
            # print('NSSSSS',ns)
            # new_data = Tracker.objects.create(api_call_time=ind_time,status=s,tracking_number=t,updated_time=u,booked=b,arrival=a,outbound=o,delivered=d,tracking_info=i,numeric_status=ns
            
            # )


            new_data = Tracker.objects.create(api_call_time=ind_time,status=s,tracking_number=t,updated_time=u,booked=b,arrival=a,outbound=o,delivered=d,tracking_info=i,numeric_status=ns
        
            )
    except:
        pass

# createfunc() 


def updatefunc():
    # request_data = requests.data
    # t = request_data['tracking_number']
    # print(track)
    te = track()
    # print(te['data']['items'][0]['status'],'ttttttt')
    new_dict=  te['data']['items']
    print(len(new_dict))
    # x = new_dict['destination_info']['trackinfo']
    # print(x)
    new_temp = []
    try:
        for i in new_dict:
            status = i['status']
            tracking_number = i['tracking_number']
            updated_time = i['updated_at']
            tracking_info = i['destination_info']['trackinfo']
            origin_info = i['origin_info']['trackinfo']
            last_event = i['lastEvent']
            if tracking_info is None:
                # print(tracking_number,'ORIGIN INFO TRACK')
                booked = ""
                outbound_date= ""
                arrival_date= ""
                delivered_date= ""
                tracking_info = ""
                new_status = ""
                if origin_info:
                    for new_t in origin_info:
                        date = new_t['Date']
                        status_desc = new_t['StatusDescription']
                        details = new_t['Details']
                        # print('OROGINNN DATE AND STATUS',tracking_number,date,status_desc)
                        if "Booked" in status_desc or "Booked,Air" in status_desc: 
                                ## Changed to CONTAINS
                            # print('STATUSS DESC',tracking_number,status_desc)
                            booked = date
                        # else:
                        #     if "Item Booked,Air" in status_desc:
                        #         print('STATUSS DESC',status_desc)
                                # booked = date
                        if "Item Received" in status_desc and "KAWASAKI" in details:
                            arrival_date = date

                        if "(Otb)" in status_desc:
                            outbound_date = date

                        if "Delivery Confirmed" in status_desc:
                            delivered_date = date

                            
                        if "TOKYO INT BAG" in details:
                            # print('ORIGIN DETAAILLSSS',tracking_number,details,status_desc)
                            new_status = "Returned"                     

                json = {
                    "new_status":new_status,
                    "tracking":tracking_number,
                    "booked":booked,
                    "outbound":outbound_date,
                    "arrival":arrival_date,
                    "delivered":delivered_date,
                },
                # print(json)

                
            elif tracking_info is not None:
                booked = ""
                outbound_date= ""
                arrival_date= ""
                delivered_date= ""
                new_status = ""
                for t in tracking_info:
                    date = t['Date']
                    status_desc = t['StatusDescription']
                    details = t['Details']
                    if "Posting/Collection " in status_desc:
                        booked = date
                    # if booked == "":
                    #     for new_t in origin_info:
                    #         date = new_t['Date']
                    #         status_desc = new_t['StatusDescription']
                    #         # print('OROGINNN DATE AND STATUS',date,status_desc)
                    #         if status_desc == "Item Bagged":
                    #             print('STATUSS DESC',status_desc,date)
                    #             booked = date
                    if "Dispatch from outward office of exchange " in status_desc:
                        outbound_date = date
                    if "Arrival at inward office of exchange " in status_desc:
                        arrival_date = date
                    if "Final delivery " in status_desc:
                        delivered_date = date
                
                if booked == "":
                    # print('EMPTYYY BOOKED',booked)
                    for j in origin_info:
                        date = j['Date']
                        status_desc = j['StatusDescription']
                        # print('ORIGN BOOK',status_desc)
                        if "Booked,Air" in status_desc:
                            print('STATUSS DESC',status_desc,date)
                            booked = date

                    # if "TOKYO INT BAG" in details:
                    #     print('ORIGIN DETAAILLSSS',tracking_number,details,status_desc)
                    #     new_status = "Returned"  
                    # if "TOKYO" in details:
                    #     print('DETAAILLSSS',details)          
                    
                
                json2 = {
                    "new_Status":new_status,
                    "tracking":tracking_number,
                    "booked":booked,
                    "outbound":outbound_date,
                    "arrival":arrival_date,
                    "delivered":delivered_date,
                },
                # print(json2)
            if new_status:              ####   Staus handling if booked and item delivery is confirmed
                status = "Returned"
            else :
                if status == "delivered":              ####   Staus handling if booked and item delivery is confirmed
                    status = "Delivered"
                else:
                    if delivered_date:
                        status = "Delivered"
                    elif arrival_date:
                        status = "Arrival"
                    elif outbound_date:
                        status = "OutBound"
                    elif booked:
                        status = "Booked"
                    elif new_status:
                        status = "Returned"
                # print(booked,'ORIGN BOOK')
            # if booked == "":
            #     print('1',booked)
            #     for new_t in origin_info:
            #         print("PPPPPP")
            #         date = new_t['Date']
            #         status_desc = new_t['StatusDescription']
            #         print('ORIGN BOOK',status_desc)
            #         if "Booked" in status_desc:
            #             print('STATUSS DESC',status_desc,date)
                            # booked = date
                            # print('ORIGN BOOK',booked)
                            # booked = dateß
                            # print('CHAL GYA BHAI')
                                

            d = {
                "status": status,
                "tracking_number":tracking_number,
                "updated_time":updated_time,    
                "Booked":booked,
                "OutBound":outbound_date,
                "Arrival":arrival_date,
                "Delivered":delivered_date,
                "lastEvent":last_event,
                # "origin_info":origin_info,
                "tracking_info":tracking_info

            }
            new_temp.append(d)

        

        for new in new_temp:
            s = new['status']
            if s == "notfound":
                s = "Available"
            # if s == "expired":
            #     Tracker.objects.update(bad=True)
            t = new['tracking_number']
            u =new['updated_time']
            b = new['Booked']
            a = new['Arrival']
            d = new['Delivered']
            o = new['OutBound']
            i = new['tracking_info']
            if d:
                s = "Delivered"
            elif o:
                s = "Outbound"
            elif a:
                s = "Arrived"
            elif b:
                s = "Booked"
            
            # print(s)

            # if b is None:
            #     pass
            # else:
            #     s = "Booked"
            #     break
            

            # if a is None:
            #     pass
            # else:
            #     s = "Arrived"
            #     break


            # if o is None:
            #     pass
            # else:
            #     s = "Outbound"
            #     break
            


            
            

            ind_time = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S.%f')
            # print('REEEACHED HEREEEEE GETDETAILS')
        #     for new_t in new_dict:
        #           tracking_number = new_t['tracking_number']
        #           Tracker.objects.filter(tracking_number=new_t).update(api_call_time=ind_time,status=s,updated_time=u,booked=b,arrival=a,outbound=o,delivered=d,tracking_info=i

        
        
        # )




            # print(current_time)


            if s == "Available":
                ns = "0"
            if s == "transit":
                ns = "1"                    
            elif s == "hold":
                ns = "2"
            elif s == "shipped":
                ns = "3"
            elif s =="expired":
                ns = "4"
            elif s == "Booked":
                ns = "5"
            elif s == "Outbound":
                ns = "6"
            elif s == "Arrived":
                ns = "7"
            elif s == "Delivered":
                ns = "8"
            
            # print('NSSSSS',ns)
            # new_data = Tracker.objects.create(api_call_time=ind_time,status=s,tracking_number=t,updated_time=u,booked=b,arrival=a,outbound=o,delivered=d,tracking_info=i,numeric_status=ns
            
            # )
            ind_time = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S.%f')
            for new_t in new_dict:
                tracking = new_t['tracking_number']
                Tracker.objects.filter(tracking_number=tracking).update(api_call_time=ind_time,status=s,updated_time=u,booked=b,arrival=a,outbound=o,delivered=d,tracking_info=i

        
        
        )

            # new_data = Tracker.objects.create(api_call_time=ind_time,status=s,tracking_number=t,updated_time=u,booked=b,arrival=a,outbound=o,delivered=d,tracking_info=i,numeric_status=ns
        
            # )
    except:
        pass


# updatefunc()