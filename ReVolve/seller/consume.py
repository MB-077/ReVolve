import requests

API_URL = 'http://127.0.0.1:8000/matching-products/'

response = requests.post(API_URL)

print(f'Status Code: {response.status_code}')
print('Response JSON:')
print(response.json())
