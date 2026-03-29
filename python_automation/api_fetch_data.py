import requests

response=requests.get("https://api.github.com")
data=response.json()

with open("api_output.txt", "w") as file: 
     file.write(str(data))

print("API data saved to file")






