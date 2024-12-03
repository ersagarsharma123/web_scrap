import requests
from bs4 import BeautifulSoup
import json

def scrape_stubhub_sports_events(url):
    try:
        # Send a GET request to the URL
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        # print(response.content)
        # print("++++++++++++++++++++++++++++++++++++++")

        # Check if the request was successful
        if response.status_code != 200:
            print(f"Failed to fetch the webpage. Status code: {response.status_code}")
            return

        # Parse the HTML content
        soup = BeautifulSoup(response.content, "html.parser")
        data = soup.find('ul').findAll('li')
        print('================\n\n\n')
        print(data)
        print('=======\n\n\n\n\n')
        test = soup.findAll('li')  # Replace 'sc-ixiy8f-2' with the exact class if needed
        print('test=\n', test)
        # tt = soup.
        print('*******************')
        # print(tt)
        # print(soup.title)
        # Extract sports events data
        events = []
        event_cards = soup.select(".event-card")  # Assuming event cards have a class name like 'event-card'
        # event_cards = soup.select(".sc-1lyqsii-6 kSnigt sc-1xjy8df-1 kTiUch")  # Assuming event cards have a class name like 'event-card'
        # print('event_cards=', event_cards)
        for card in event_cards[:5]:  # Limit to 5 events
            title = card.select_one(".event-title").text.strip() if card.select_one(".event-title") else "N/A"
            datetime = card.select_one(".event-datetime").text.strip() if card.select_one(".event-datetime") else "N/A"
            location = card.select_one(".event-location").text.strip() if card.select_one(".event-location") else "N/A"
            image = card.select_one("img")['src'] if card.select_one("img") else "N/A"

            events.append({
                "title": title,
                "datetime": datetime,
                "location": location,
                "image": image
            })

        # Convert the events data to JSON
        events_json = json.dumps(events, indent=4)
        return events_json

    except Exception as e:
        print(f"An error occurred: {e}")

# URL to scrape
url = "https://www.stubhub.com/explore?lat=MjUuNDQ3ODg5OA%3D%3D&lon=LTgwLjQ3OTIyMzY5OTk5OTk5&to=253402300799999&tlcId=2"
# url = "https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/"

# Scrape the events and print the JSON data
sports_events_json = scrape_stubhub_sports_events(url)
# if sports_events_json:
#     print(sports_events_json)
