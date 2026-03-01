from requests import get
from json import dump, load, decoder
from webhook import webhook
from dotenv import load_dotenv
from os import getenv
from time import sleep
from random import randint
from geo_check import is_in
    
coords = [(17.9023521, 59.295544),
            (18.0020611, 59.363135),
            (18.0971011, 59.369088),
            (18.1686171, 59.323611),
            (18.1612161, 59.251646),
            (18.0854581, 59.221866)]

load_dotenv()
url = getenv("bf_url")
r = get(url)
data = r.json()

"""with open("data.json", "w", encoding="utf-8") as f:
    dump(data, f, indent=4, ensure_ascii=False)"""

try:
    with open("prospects.json", "r", encoding="utf-8") as f:
        prospects = load(f)
        # print(prospects)
except decoder.JSONDecodeError:
    prospects = []

def desirable(size, price, student, long, lat):
    if student == True and price <= 6097 and size >= 23 and is_in(long, lat, coords):
        return True
    else:
        return False

def search(obj, single=True):
    if single == True:
        size = obj.get("Yta")
        price = obj.get("Hyra")
    else:
        size = obj.get("LägstaYtan")
        price = obj.get("LägstaHyran")
    id = obj.get("LägenhetId")
    long = obj.get("KoordinatLongitud")
    lat = obj.get("KoordinatLatitud")
    address = obj.get("Gatuadress")
    where = obj.get("Stadsdel")
    student_type = obj.get("Student")
    date = obj.get("AnnonseradTill")

    if obj not in prospects:
        if desirable(size, price, student_type, long, lat):
            # Skicka notis i discord embed
            webhook(title=f"{where}, {address}", description=f"Ny annons hittad. Pris: {price} kr. Storlek: {size} kvm. Annonseras till {date}.", url=f"https://bostad.stockholm.se/bostad/{id}")
            prospects.append(obj)
            with open("prospects.json", "w", encoding="utf-8") as f:
                dump(prospects, f, indent=4, ensure_ascii=False)

def main():
    while True:
        for obj in data:
            try:
                count = obj.get("Antal")
                if count == 1:
                    search(obj, single=True)
                else:
                    search(obj, single=False)
            except Exception as error:
                print(f"Error processing object no {id}: {error}")
        sleep_time = randint(1800, 7200)
        print(f"Sleeping for {sleep_time//60} minutes...")
        sleep(sleep_time)
main()