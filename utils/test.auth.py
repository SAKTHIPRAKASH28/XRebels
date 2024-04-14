import requests

# Replace 'YOUR_JWT_TOKEN_HERE' with your actual JWT token
jwt_token = {
    "Token": "eyJhbGciOiJSUzI1NiIsImtpZCI6ImYyOThjZDA3NTlkOGNmN2JjZTZhZWNhODExNmU4ZjYzMDlhNDQwMjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20veHJlYmVscy01YzdhNCIsImF1ZCI6InhyZWJlbHMtNWM3YTQiLCJhdXRoX3RpbWUiOjE3MTMwNjA3MDEsInVzZXJfaWQiOiJ3WXRXZUpuZk8zUTcyNm1xNDlTNWdzaXZ2ZjcyIiwic3ViIjoid1l0V2VKbmZPM1E3MjZtcTQ5UzVnc2l2dmY3MiIsImlhdCI6MTcxMzA2MDcwMSwiZXhwIjoxNzEzMDY0MzAxLCJlbWFpbCI6InVzZXJAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJmaXJlYmFzZSI6eyJpZGVudGl0aWVzIjp7ImVtYWlsIjpbInVzZXJAZ21haWwuY29tIl19LCJzaWduX2luX3Byb3ZpZGVyIjoicGFzc3dvcmQifX0.lVqblWUJK-qRBJsUal63k3Q9TMMiYgUKn-3LdeflzJ3Ej8oH9mSSZCSTaqnhA1wYwf-aPCq3FOt_I28g2-xnGp1pdKN42ZNvIo0-VLLeiHCONotp-QS1XE9fsIhLtojvpkGqtGQGWktEHPYBQzpI5lRZ-4hUwk7RXqaOiiHDotHhrzQ9w1ka7tZgGTK1efXutqrbNyFYCCYgOAfpxpu8sjoRF5vxGDT0-IPmMMMqRTlZNXFDxd636s_Rb7ATgvMRb8pPLrPqs2n9V5WOCRGmdI4YKqQLRnCg7uUkxrRRf_fQyEsoh-VxILA_86kS3Mci6i39D9Zjn-TCqccqVk3ufA"
}
# URL of the endpoint
url = 'http://localhost:8000/auth'  # Change the URL if necessary

# Headers containing the JWT token
headers = {
    'Authorization': jwt_token["Token"]
}

# Sending the request
response = requests.get(url, headers=headers)

# Checking the response status
if response.status_code == 200:
    print("User ID:", response.text)
else:
    print("Error:", response.status_code, response.text)
