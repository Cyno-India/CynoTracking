



import requests
from msbctracker.models import Tracker
from msbctracker.views import track

def get():
    request_data = requests.data
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
        
        print('NSSSSS',ns)
        # new_data = Tracker.objects.create(api_call_time=ind_time,status=s,tracking_number=t,updated_time=u,booked=b,arrival=a,outbound=o,delivered=d,tracking_info=i,numeric_status=ns
        
        # )


        new_data = Tracker.objects.create(api_call_time=ind_time,status=s,tracking_number=t,updated_time=u,booked=b,arrival=a,outbound=o,delivered=d,tracking_info=i,numeric_status=ns
    
)

# except:
#     pass    
# ttt = Tracker.objects.all().values()
# print('tttttt',ttt)
    # return Response('Error')
    # print(new_dict)
    print(new_data)


get()

