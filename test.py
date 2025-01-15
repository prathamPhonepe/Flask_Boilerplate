import requests
import random
import string

url = "https://web.ktkpp.com/backend/users/api/v1/profile/update"  

url2 = "https://web.ktkpp.com/backend/users/api/v1/get_wallet"

headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiJVNGM5YmYwOTg5YzhlNDJiYzkxYmU1MGU2ZTQxMjdjMWMiLCJleHAiOjE3NTQ5MjAxNjB9.bPAur2NyS5rJgcU-_VEOsaHZqI5sOpBxdIM8IX95xOw",
    "Content-Type": "application/json"
}

def generate_random_address(length=20):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def send_requests():
    for i in range(100):
        random_address = generate_random_address()
        
        data = {
            "address": random_address,
            "first_name": "Test",
            "last_name": "Test S",
            "uid": "U4c9bf0989c8e42bc91be50e6e4127c1c" , 

            
             }
        
        response = requests.put(url, json=data, headers=headers)
        response2 = requests.get(url2, headers=headers)

        
        print(f"Request {i + 1}: Status Code: {response.status_code}, Response: {response.text}")
        print(f"Request {i + 1}: Status Code: {response2.status_code}, Response2: {response2.text}")


# Run the script
send_requests()
