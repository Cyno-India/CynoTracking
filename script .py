# list_a = [
#                         {
#                             "StatusDescription": "Item Delivery Confirmed,Air",
#                             "Date": "2022-12-30 12:28:00",
#                             "Details": "Japan,3400199",
#                             "checkpoint_status": "delivered",
#                             "substatus": "delivered001"
#                         },
#                         {
#                             "StatusDescription": "Item Received,Air",
#                             "Date": "2022-12-30 07:18:00",
#                             "Details": "Japan,3400199",
#                             "checkpoint_status": "transit",
#                             "substatus": "transit001"
#                         },
#                         {
#                             "StatusDescription": "Item Dispatched,Air",
#                             "Date": "2022-12-29 12:00:00",
#                             "Details": "Japan,KAWASAKI HIGASHI",
#                             "checkpoint_status": "transit",
#                             "substatus": "transit002"
#                         },
#                         {
#                             "StatusDescription": "Item Dispatched,Air",
#                             "Date": "2022-12-29 11:59:00",
#                             "Details": "Japan,NARITA AP A",
#                             "checkpoint_status": "transit",
#                             "substatus": "transit002"
#                         },
#                         {
#                             "StatusDescription": "Item Received,Air",
#                             "Date": "2022-12-28 08:59:00",
#                             "Details": "Japan,KAWASAKI HIGASHI",
#                             "checkpoint_status": "transit",
#                             "substatus": "transit001"
#                         },
#                         {
#                             "StatusDescription": "Item Received,Air",
#                             "Date": "2022-12-28 02:16:00",
#                             "Details": "Japan,KAWASAKI HIGASHI",
#                             "checkpoint_status": "transit",
#                             "substatus": "transit001"
#                         },
#                         {
#                             "StatusDescription": "Item Bagged,Air",
#                             "Date": "2022-12-23 11:35:48",
#                             "Details": "India,DELHI INTERNATIONAL MAIL CENTRE",
#                             "checkpoint_status": "transit",
#                             "substatus": "transit001"
#                         },
#                         {
#                             "StatusDescription": "Item Received,Air",
#                             "Date": "2022-12-23 11:34:47",
#                             "Details": "India,DELHI INTERNATIONAL MAIL CENTRE",
#                             "checkpoint_status": "transit",
#                             "substatus": "transit001"
#                         },
#                         {
#                             "StatusDescription": "Item Dispatched,Air",
#                             "Date": "2022-12-22 20:22:53",
#                             "Details": "India,New Delhi Foreign Post Booking Coun",
#                             "checkpoint_status": "transit",
#                             "substatus": "transit002"
#                         },
#                         {
#                             "StatusDescription": "Item Bagged,Air",
#                             "Date": "2022-12-22 17:48:48",
#                             "Details": "India,New Delhi Foreign Post Booking Coun",
#                             "checkpoint_status": "transit",
#                             "substatus": "transit001"
#                         },
#                         {
#                             "StatusDescription": "Item Booked,Air",
#                             "Date": "2022-12-22 16:08:14",
#                             "Details": "India,New Delhi Foreign Post Booking Coun",
#                             "substatus": "notfound001",
#                             "checkpoint_status": "transit"
#                         }
#                     ]
# list_b=   [
#                         {
#                             "Date": "2022-12-30 12:28:00",
#                             "StatusDescription": "Final delivery ",
#                             "Details": "SATTE,SAITAMA,340-0199",
#                             "checkpoint_status": "delivered",
#                             "substatus": "delivered001"
#                         },
#                         {
#                             "Date": "2022-12-30 07:18:00",
#                             "StatusDescription": "Processing at delivery Post Office ",
#                             "Details": "SATTE,SAITAMA,340-0199",
#                             "checkpoint_status": "transit",
#                             "substatus": "transit001"
#                         },
#                         {
#                             "Date": "2022-12-29 12:00:00",
#                             "StatusDescription": "Departure from inward office of exchange ",
#                             "Details": "KAWASAKIHIGASHI,KANAGAWA,219-8799",
#                             "checkpoint_status": "transit",
#                             "substatus": "transit001"
#                         },
#                         {
#                             "Date": "2022-12-28 09:00:00",
#                             "StatusDescription": "Held by import Customs ",
#                             "Details": "KAWASAKIHIGASHI,KANAGAWA,219-8799",
#                             "checkpoint_status": "transit",
#                             "substatus": "transit001"
#                         },
#                         {
#                             "Date": "2022-12-28 02:16:00",
#                             "StatusDescription": "Arrival at inward office of exchange ",
#                             "Details": "KAWASAKIHIGASHI,KANAGAWA,219-8799",
#                             "checkpoint_status": "transit",
#                             "substatus": "transit004"
#                         },
#                         {
#                             "Date": "2022-12-23 11:35:00",
#                             "StatusDescription": "Dispatch from outward office of exchange ",
#                             "Details": "DELHI INTERNATIONAL MAIL CENTRE,INDIA",
#                             "checkpoint_status": "transit",
#                             "substatus": "transit001"
#                         },
#                         {
#                             "Date": "2022-12-23 11:34:00",
#                             "StatusDescription": "Arrival at outward office of exchange ",
#                             "Details": "DELHI INTERNATIONAL MAIL CENTRE,INDIA",
#                             "checkpoint_status": "transit",
#                             "substatus": "transit002"
#                         }
#                     ]

# # def get_difference(list_a, list_b):
# #     non_match_a  = set(list_a)-set(list_b)
# #     non_match_b  = set(list_b)-set(list_a)
# #     non_match = list(non_match_a) + list(non_match_b)
# #     return non_match


# # get_difference(list_a, list_b)
# # print("Non-match elements: ", non_match)
# for i in list_a:
#         if i not in list_b:
#             print(i)




import pandas as pd
pd.read_json("/path/to/json/file").to_excel("output.xlsx")
