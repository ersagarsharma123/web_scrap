import scrapy
import json

class StubHubSpider(scrapy.Spider):
    name = "stubhub_spider"
    start_urls = [
        "https://www.stubhub.com/explore?lat=MjUuNDQ3ODg5OA%3D%3D&lon=LTgwLjQ3OTIyMzY5OTk5OTk5&to=253402300799999&tlcId=2"
    ]

    def parse(self, response):
        # List to store event details
        events = []

        # Use XPath or CSS selectors to extract data
        event_cards = response.css(".event-card")  # Update selector based on the webpage structure

        for card in event_cards[:5]:  # Extract only the first 5 events
            title = card.css(".event-title::text").get(default="N/A").strip()
            datetime = card.css(".event-datetime::text").get(default="N/A").strip()
            location = card.css(".event-location::text").get(default="N/A").strip()
            image = card.css("img::attr(src)").get(default="N/A")

            events.append({
                "title": title,
                "datetime": datetime,
                "location": location,
                "image": image
            })

        # Save the extracted data to a JSON file
        with open("events.json", "w") as f:
            json.dump(events, f, indent=4)

        self.log(f"Saved {len(events)} events to events.json")
