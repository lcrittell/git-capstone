import requests

API_KEY = "no"

url = "https://api.tcgapi.dev/v1/search"

headers = {
    "X-API-Key": API_KEY
}

params = {
    "q": "The Hobbit",
    "game": "magic",
    "type": "Sealed Products",
    "per_page": 100
}

response = requests.get(
    url,
    params=params,
    headers=headers
)

response.raise_for_status()

data = response.json()

for product in data["data"]:
    if (
        product["set_name"] == "The Hobbit"
        and product["name"] == "The Hobbit - Play Booster Pack"
        and product["product_type"] == "Sealed Products"
    ):
        print(f"Product: {product['name']}")
        print(f"Market Price: ${product['market_price']}")