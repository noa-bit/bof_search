import requests
from dotenv import load_dotenv
import os

load_dotenv()
URL = os.getenv("WEBHOOK_URL")

def webhook(title, description, color=0x3498db, fields=None):

    payload = {"embeds": [{
        "title": title,
        "description": description,
        "color": color,
        #"fields": fields or []
        }]
    }

    response = requests.post(URL, json=payload)
    
    if response.status_code == 204:
        print("Notification sent!")
    else:
        print(f"Failed: {response.status_code} - {response.text}")

webhook(title="hej", description="beskrivning")