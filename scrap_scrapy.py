import requests
from bs4 import BeautifulSoup

url = "https://www.stubhub.com/explore?lat=MjUuNDQ3ODg5OA%3D%3D&lon=LTgwLjQ3OTIyMzY5OTk5OTk5&to=253402300799999&tlcId=2"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
print(soup.prettify())

for para in soup.find_all('div'):
    print(para)