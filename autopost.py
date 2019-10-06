import requests
import random
import json
from datetime import datetime
from dateutil.tz import gettz
import time

statusList = ['online', 'offline']
f = open('settings.json', "r")

settings = json.loads(f.read())

response = requests.post(url=settings['server_url']+'/login', data=settings)
authResponse = response.json()

# print(authResponse)

authToken = authResponse['token']
headers = {'Authorization': 'Bearer ' + authToken}

deviceId = input('Enter deviceId whose data is to be spammed : ')

while True:
    try:
        chosenStatus = random.choice(statusList)
        randomLoad = float(random.uniform(15.0, 50.5))
        currentDatetime = datetime.now(gettz("Asia/Kolkata")).isoformat()

        data = {
            'deviceId': deviceId,
            'status': chosenStatus,
            'time': currentDatetime,
            'load': randomLoad,
        }
        
        response = requests.post(url=settings['server_url']+'/monitor',
                    data=data,
                    headers=headers
                )
        print(response.json())
        print("Press Ctrl+C to exit")
        time.sleep(settings['interval'])
        
    except KeyboardInterrupt:
        exit()




