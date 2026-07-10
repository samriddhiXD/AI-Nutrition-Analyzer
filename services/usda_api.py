import requests
from config import USDA_API_KEY

BASE_URL = "https://api.nal.usda.gov/fdc/v1/foods/search"


def search_food(food_name):
    """
    Search food using USDA FoodData Central API.
    Returns nutrition information for the first matching food.
    """

    params = {
        "query": food_name,
        "api_key": USDA_API_KEY,
        "pageSize": 1
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()

        data = response.json()

        if not data.get("foods"):
            return None

        food = data["foods"][0]

        nutrients = {
            "Calories": 0,
            "Protein": 0,
            "Fat": 0,
            "Carbohydrates": 0,
            "Fiber": 0,
            "Sugar": 0
        }

        for nutrient in food.get("foodNutrients", []):

            name = nutrient.get("nutrientName")
            value = nutrient.get("value", 0)

            if name == "Energy":
                nutrients["Calories"] = value

            elif name == "Protein":
                nutrients["Protein"] = value

            elif name == "Total lipid (fat)":
                nutrients["Fat"] = value

            elif name == "Carbohydrate, by difference":
                nutrients["Carbohydrates"] = value

            elif name == "Fiber, total dietary":
                nutrients["Fiber"] = value

            elif name == "Sugars, total including NLEA":
                nutrients["Sugar"] = value

        return {
            "food_name": food.get("description"),
            "serving_size": food.get("servingSize", "N/A"),
            "serving_unit": food.get("servingSizeUnit", ""),
            "calories": nutrients["Calories"],
            "protein": nutrients["Protein"],
            "fat": nutrients["Fat"],
            "carbs": nutrients["Carbohydrates"],
            "fiber": nutrients["Fiber"],
            "sugar": nutrients["Sugar"]
        }

    except requests.exceptions.RequestException as e:
        print("API Error:", e)
        return None