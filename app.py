from flask import Flask, render_template, request, redirect, url_for

from models.database import (
    create_table,
    add_meal,
    get_all_meals,
    get_today_totals
)

from services.usda_api import search_food
from utils.recommendation import generate_recommendation

app = Flask(__name__)

# Create database table
create_table()


@app.route("/")
def home():
    return render_template(
        "index.html",
        food=None,
        error=None
    )


@app.route("/search", methods=["POST"])
def search():

    food_name = request.form.get("food_name")

    if not food_name:
        return render_template(
            "index.html",
            food=None,
            error="Please enter a food name."
        )

    food = search_food(food_name)

    if food is None:
        return render_template(
            "index.html",
            food=None,
            error="Food not found."
        )

    return render_template(
        "index.html",
        food=food,
        error=None
    )


@app.route("/add", methods=["POST"])
def add():

    add_meal(
        request.form["food_name"],
        request.form["meal_type"],
        float(request.form["calories"]),
        float(request.form["protein"]),
        float(request.form["fat"]),
        float(request.form["carbs"]),
        float(request.form["fiber"]),
        float(request.form["sugar"]),
        request.form["quantity"]
    )

    return redirect(url_for("tracker"))


@app.route("/tracker")
def tracker():

    meals = get_all_meals()
    totals = get_today_totals()

    recommendations = generate_recommendation(
        totals["calories"],
        totals["protein"],
        totals["fat"],
        totals["carbs"],
        totals["fiber"],
        totals["sugar"]
    )

    return render_template(
        "tracker.html",
        meals=meals,
        totals=totals,
        recommendations=recommendations
    )


@app.route("/dashboard")
def dashboard():

    totals = get_today_totals()

    return render_template(
        "dashboard.html",
        totals=totals
    )


if __name__ == "__main__":
    app.run(debug=True)