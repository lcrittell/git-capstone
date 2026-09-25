from src.api.tcg_api import get_play_booster
import json
import os

pack_prices = []

pack_prices.append({
    "set": "The Hobbit",
    "product": "Test set play booster",
    "market_price": 70.00,
    "tcgplayer_id": 1,
    "price_updated_at": "2026-09-24T22:09:17.285Z"
})

pack_prices.append({
    "set": "Secrets of Strixhaven",
    "product": "Test set play booster",
    "market_price": 70.00,
    "tcgplayer_id": 1,
    "price_updated_at": "2026-09-24T22:09:17.285Z"
})

pack_prices.append({
    "set": "Lorwyn Eclipsed",
    "product": "Test set play booster",
    "market_price": 70.00,
    "tcgplayer_id": 1,
    "price_updated_at": "2026-09-24T22:09:17.285Z"
})

with open("backend/data/sealed_prices.json", "w") as file:
    json.dump(pack_prices, file, indent=4)

print("Pack prices updated.")