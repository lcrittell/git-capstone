import json
from pathlib import Path

from fastapi import APIRouter

router = APIRouter(prefix="/api")

DATA_FILE = Path(__file__).resolve().parents[2] / "data" / "sealed_prices.json"


@router.get("/pack-prices")
def get_pack_prices():

    with open(DATA_FILE, "r") as file:
        sealed_prices = json.load(file)

    sealed_prices_by_set = {
        product["set"]: product["market_price"]
        for product in sealed_prices
    }

    return [
        {
            "set": "The Hobbit",
            "pack_price": sealed_prices_by_set.get("The Hobbit"),
            "average_card_value": 7.50,
            "estimated_return": 7.50,
        },
        {
            "set": "Secrets of Strixhaven",
            "pack_price": sealed_prices_by_set.get("Secrets of Strixhaven"),
            "average_card_value": 6.25,
            "estimated_return": 6.25,
        },
        {
            "set": "Lorwyn Eclipsed",
            "pack_price": sealed_prices_by_set.get("Lorwyn Eclipsed"),
            "average_card_value": 3.80,
            "estimated_return": 3.80,
        },
    ]