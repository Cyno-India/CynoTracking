# from . functions import track
from datetime import datetime
from pytz import timezone 
import requests

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
    api_url = "https://api.tracktry.com/v1/trackings/get"
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
        print('TRACKINGGGGG INFOOO TYPEE',type(tracking_info))
        print('ORRRIGGGNN INFOOO TYPEE',type(origin_info))
        if tracking_info and origin_info:
            # new_info = tracking_info - origin_info
            new_info_data = [i for i, j in zip(tracking_info, origin_info) if i == j]
            print('NEWWWWWW INFOOOO DAATAAAAAA',new_info_data)
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