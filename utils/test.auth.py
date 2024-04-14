import requests

# Replace 'YOUR_JWT_TOKEN_HERE' with your actual JWT token
jwt_token = {
    "Token": "eyJhbGciOiJSUzI1NiIsImtpZCI6ImYyOThjZDA3NTlkOGNmN2JjZTZhZWNhODExNmU4ZjYzMDlhNDQwMjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20veHJlYmVscy01YzdhNCIsImF1ZCI6InhyZWJlbHMtNWM3YTQiLCJhdXRoX3RpbWUiOjE3MTMwOTYzMDcsInVzZXJfaWQiOiJWdjhDWVBVTEQ2VW51b05Lb3RURlFZTmRwZEsyIiwic3ViIjoiVnY4Q1lQVUxENlVudW9OS290VEZRWU5kcGRLMiIsImlhdCI6MTcxMzA5NjMwNywiZXhwIjoxNzEzMDk5OTA3LCJlbWFpbCI6InNha3RoaXByYWthc2hAc3R1ZGVudC50Y2UuZWR1IiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJmaXJlYmFzZSI6eyJpZGVudGl0aWVzIjp7ImVtYWlsIjpbInNha3RoaXByYWthc2hAc3R1ZGVudC50Y2UuZWR1Il19LCJzaWduX2luX3Byb3ZpZGVyIjoicGFzc3dvcmQifX0.RK9AsGOQcD-TyrX2s2z7dV6_Mwp6nLcKw3EvsIm1D1a1LiatGql5L8uCG4tFuzYRHnnRpt__aan9eAameonldtxnL1Q7JsfLBK5LN_agIqRmSJM9KEFZhBJZLHFs8AbvT9qymXwx3zYchKzJw8oExE8XYXhmX9I9Ted22mai86cjHaUUPpdcClWtmFk2HJturXpDpYxjBh-qzWozLkZrfi4uLXVATp25A4FZ_RGEtFKmobk3VTM6qhaYoDaF0An4zKAgUvu6UukCnRt6wDo10DEH3LUALQAr7a74BeNIfEDrK0mIOkkB0TuxTqmifDGI44gPnEbDUmKaFlxNcDhh1Q"
}
# URL of the endpoint
url = 'http://localhost:8000/chat/'  # Change the URL if necessary

# Headers containing the JWT token
headers = {
    'authorization': jwt_token["Token"]
}
body = {
    "prompt": "Hii!Im Sakthi"
}

# Sending the request
response = requests.post(url, body, headers=headers)

# Checking the response status
if response.status_code == 200:
    print("User ID:", response.text)
else:
    print("Error:", response.status_code, response.text)
