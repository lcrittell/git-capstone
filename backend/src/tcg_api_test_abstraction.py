import requests

API_KEY = "no"

url = "https://api.tcgapi.dev/v1/search"

headers = {
    "X-API-Key": API_KEY
}


def get_play_booster(set_name):
    params = {
        "q": set_name,
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
        #print(product)
        if (
            product["set_name"] == set_name
            and "Play Booster Pack" in product["name"]
        ):
            return product

    return None


product = get_play_booster("FINAL FANTASY")

if product:
    print(f"Product: {product['name']}")
    print(f"Market Price: ${product['market_price']}")
    print(f"TCGplayer ID: {product['tcgplayer_id']}")
    print(f"Price Updated: {product['price_updated_at']}")
else:
    print("Play Booster Pack not found.")