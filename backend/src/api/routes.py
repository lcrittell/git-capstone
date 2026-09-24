from fastapi import APIRouter

router = APIRouter(prefix="/api")


@router.get("/pack-prices")
def get_pack_prices():
    return [
        {
            "set": "Example Set",
            "pack_price": 700.99,
            "average_card_value": 7.50,
            "estimated_return": 7.50,
        },
        {
            "set": "Test Set",
            "pack_price": 4.99,
            "average_card_value": 6.25,
            "estimated_return": 6.25,
        },
        {
            "set": "Sample Set",
            "pack_price": 4.99,
            "average_card_value": 3.80,
            "estimated_return": 3.80,
        },
    ]