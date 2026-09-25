from src.api.tcg_api import get_play_booster
import json
import os

API_KEY = os.environ["TCG_API"]
print(f"API key loaded: {bool(API_KEY)}")

sets = [
    "The Hobbit",
    "Secrets of Strixhaven",
    "Lorwyn Eclipsed",
]

pack_prices = []

for set_name in sets:
    product = get_play_booster(set_name, API_KEY)

    if product:
        print(f"{set_name}: ${product['market_price']}")

        pack_prices.append({
            "set": set_name,
            "product": product["name"],
            "market_price": product["market_price"],
            "tcgplayer_id": product["tcgplayer_id"],
            "price_updated_at": product["price_updated_at"]
        })
    else:
        print(f"{set_name}: Play Booster Pack not found")

with open("backend/data/sealed_prices.json", "w") as file:
    json.dump(pack_prices, file, indent=4)

print("Pack prices updated.")