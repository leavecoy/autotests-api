import httpx

login_payload = {
    "email": "aylo@example.com",
    "password": "123"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login",json=login_payload)

login_response_data = login_response.json()

me_payload = {"refreshToken": login_response_data['token']['accessToken']}

me_response = httpx.post("http://localhost:8000/api/v1/authentication/refresh", json=me_payload)
me_response_data = me_response.json()

print("Me response:", me_response_data)
print("Me StatusCode:", me_response.status_code)