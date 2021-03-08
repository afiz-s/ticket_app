import requests
from faker import Faker
from random import randint
import time

fake = Faker()

count = int(input("how many record you want to generate? "))
for _ in range(count):
    customer_name = fake.name()
    performance_title = fake.name()
    price = randint(5, 15)
    performance_time = fake.date_between(start_date='-2y', end_date='today').strftime('%Y-%m-%d %H:%M:%S.%f')
    url = 'http://localhost:8000/api/tickets'
    data = {
        'customer_name': customer_name, 
        'performance_title': performance_title,
        'price': price,
        'performance_time': performance_time
    }
    try:
        requests.post(url=url, data=data)
        print('Added: ', data)
        time.sleep(1)
    except Exception as e:
        print(e)
