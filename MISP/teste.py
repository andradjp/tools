import requests as rq
from json import dumps
from datetime import datetime, timezone, timedelta

# token = 'hDGXd9yal8BN1RfHrhNUbZGAXFqg1HTDxy6E1WIf'
# headers = {'Authorization': token, 'Accept': 'application/json',
#                'Content-Type': 'application/json'}
# filter = {'event_timestamp':(datetime.now() - timedelta(hours=1)).replace(tzinfo=timezone.utc).timestamp()}
# data = rq.post('http://misp.brb.com.br/attributes/restSearch/json',data=dumps(filter),headers=headers).json()
# print(data)

# print(datetime.now().timestamp())


teste = input('Digite qualquer coisa: ')
print(teste)