from requests import get
from json import dump, load, decoder
from webhook import webhook
from dotenv import load_dotenv
import os
from time import sleep
from random import randint

def desirable(size, price, student):
    if student == True and price <= 6097 and size >= 23:
        return True
    else:
        return False

load_dotenv()
url = os.getenv("bf_url")
r = get(url)
data = r.json()

with open("data.json", "w", encoding="utf-8") as f:
    dump(data, f, indent=4, ensure_ascii=False)

try:
    with open("prospects.json", "r", encoding="utf-8") as f:
        prospects = load(f)
        # print(prospects)
except decoder.JSONDecodeError:
    prospects = []

def main():
    while True:
        for obj in data:
            try:

                id = obj.get("LägenhetId")
                size = obj.get("Yta")
                price = obj.get("Hyra")
                long = obj.get("KoordinatLongitud")
                lat = obj.get("KoordinatLatitud")
                address = obj.get("Gatuadress")
                where = obj.get("Stadsdel")
                student_type = obj.get("Student")
                date = obj.get("AnnonseradTill")

                if obj not in prospects:
                    if desirable(size, price, student_type):
                        # Skicka notis i discord embed
                        webhook(title=f"{where}, {address}", description=f"Ny annons hittad. Pris: {price} kr. Storlek: {size} kvm. Annonseras till {date}.", url=f"https://bostad.stockholm.se/bostad/{id}")
                        prospects.append(obj)
                        with open("prospects.json", "w", encoding="utf-8") as f:
                            dump(prospects, f, indent=4, ensure_ascii=False)
            except Exception as error:
                print(f"Error processing object: {error}")
        sleep(randint(1800, 7200))

main()