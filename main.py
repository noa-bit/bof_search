import requests, json
from shapely import Point, Polygon

def desirable(size, price):
    if price <= 6097 and size >= 23:
        return True
    else:
        return False

url = "https://bostad.stockholm.se/AllaAnnonser/"
r = requests.get(url)
data = r.json()

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

try:
    with open("prospects.json", "r", encoding="utf-8") as f:
        prospects = json.load(f)
        print(prospects)
except json.decoder.JSONDecodeError:
    prospects = []

def main():
    for obj in data:
        id = obj.get("LägenhetId")
        size = obj.get("Yta")
        price = obj.get("Hyra")
        long = obj.get("KoordinatLongitud")
        lat = obj.get("KoordinatLatitud")
        student_type = obj.get("Student")
        if obj not in prospects:
            print("hello")
            if desirable(size, price):
                # Skicka notis i discord embed
                prospects.append(obj)