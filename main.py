import requests, json
from shapely import Point, Polygon
from webhook import webhook

def desirable(size, price, student):
    if student == True and price <= 6097 and size >= 23:
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
        # print(prospects)
except json.decoder.JSONDecodeError:
    prospects = []

def main():
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
                    webhook(title=f"{where}, {address}", description="Ny annons hittad.",url=f"https://bostad.stockholm.se/bostad/{id}")
                    prospects.append(obj)
                    with open("prospects.json", "w", encoding="utf-8") as f:
                        json.dump(prospects, f, indent=4, ensure_ascii=False)
        except Exception as error:
            print(f"Error processing object: {error}")

main()