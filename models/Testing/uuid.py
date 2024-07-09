#!/usr/bin/python3

#using uuid to genarate random id

import uuid

myId = uuid.uuid4()
print(f'My id no: {myId}')

#Generatin current date and time
from datetime import date

today = date.today()