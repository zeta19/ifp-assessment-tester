import requests
import random
import json
from datetime import datetime
from dateutil.tz import gettz
import time

statusList = ['online', 'offline']
authToken = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyRGV0YWlscyI6eyJ1c2VyaWQiOjQsInVzZXJuYW1lIjoiamFuZSJ9LCJpYXQiOjE1NzAzNTgzMTMsImV4cCI6MTU3MDM2MDExM30.QcXzI2b_huayvkiDsrFag5HQjVEwRuK4A5ZPD20BLgc'
headers = {'Authorization': 'Bearer ' + authToken}

while True:
    chosenStatus = random.choice(statusList)
    randomLoad = float(random.uniform(15.0, 50.5))
    currentDatetime = datetime.now(gettz("Asia/Kolkata")).isoformat()

    data = {
        'deviceId': 'S10',
        'status': chosenStatus,
        'time': currentDatetime,
        'load': randomLoad,
    }
    
    response = requests.post(url='http://localhost:5000/monitor',
                data=data,
                headers=headers
            )
    print(response.json)
    time.sleep(1);    
