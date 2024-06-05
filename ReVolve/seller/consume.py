import requests

# URL of your Django API endpoint
API_URL = 'http://127.0.0.1:8000/api/seller_products/'

# # Sample data to send to the API
# data = {
#     'item_id': '123',
#     'item_name': 'Steel Rod',
#     'item_material_type': 'Steel',
#     'item_grade': 'A',
#     'item_condition': 'New',
#     'item_volume': 100.0,
#     'item_cost': 500.0,
#     'seller': 1  # Assuming '1' is the ID of an existing Seller in your database
# }

# Send POST request to the API
response = requests.post(API_URL)

# Print the response from the server
print(f'Status Code: {response.status_code}')
print('Response JSON:')
print(response.json())
