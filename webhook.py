import requests
from dotenv import load_dotenv
import os

load_dotenv()
URL = os.getenv("WEBHOOK_URL")

def webhook(title="Ny annons hittad", description="s", url="https://bostad.stockholm.se/bostad", fields=None):

    payload = {"embeds": [{
        "title": title,
        "description": description,
        "url": url
        #"fields": fields or []
        }]
    }

    response = requests.post(URL, json=payload)
    
    if response.status_code == 204:
        print("Notification sent!")
    else:
        print(f"Failed: {response.status_code},  {response.text}")

if __name__ == "__main__":
    webhook(title="hej", description="beskrivning")