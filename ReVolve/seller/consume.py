import requests

API_URL = 'http://127.0.0.1:8000/matching-products/'


# data = {
#     'item_material_type': 'Steel',
#     'item_grade': '304',
# }

# response = requests.post(API_URL, json=data)
response = requests.post(API_URL)


print(f'Status Code: {response.status_code}')
print('Response JSON:')
print(response.json())
