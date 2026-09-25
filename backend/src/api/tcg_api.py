import requests

url = "https://api.tcgapi.dev/v1/search"



def get_play_booster(set_name, api_key):
    params = {
        "q": set_name,
        "game": "magic",
        "type": "Sealed Products",
        "per_page": 100
    }

    headers = {
        "X-API-Key": api_key
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