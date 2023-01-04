
import requests


def numbers(tr):
    # track = request.get('tracking_number')
    # print(track)
    # code = request.data['carrier_code']
    # print(code)
    new_temp = []
    print('hello')
    # for i in Tracking: 
    #     # print(Tracking)
    #     # print(i)
    #     json =  {
    #         "tracking_number":Tracking,
    #         "carrier_code": "india-post"
    #     }
    #     print(json)
    #     new_temp.append(json)
    # print(new_temp)
    api_url = "https://api.tracktry.com/v1/trackings/batch"
    print("API HITTTTT")
    headers =  {"Content-Type":"application/json","Tracktry-Api-Key":"27654af3-b244-4192-b7d8-ce32be8d86c4"}
    #     # # data = {
    #     # # "tracking_number":t,
    #     # # "carrier_code": "india-post"
    #     # # }
    #     # # data = t,c

    response = requests.post(api_url, headers=headers,json=tr)
    print("RESPONSE HIT")
    print(response)
    print('hellooo')
    # print(new_temp)
    res = response.json()
    print('RESPONSE',res)
    # temp = {
    #     "status":res['data'][0]['status'],
    #     "id":res['data'][0]['id']
    # }
