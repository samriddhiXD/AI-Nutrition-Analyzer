import sqlite3
from config import DATABASE_NAME


def get_connection():
    """
    Create and return a database connection.
    """
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def create_table():
    """
    Create meals table if it doesn't exist.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS meals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            food_name TEXT NOT NULL,
            meal_type TEXT NOT NULL,
            calories REAL,
            protein REAL,
            fat REAL,
            carbs REAL,
            fiber REAL,
            sugar REAL,
            quantity TEXT,
            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def add_meal(food_name, meal_type, calories, protein, fat,
             carbs, fiber, sugar, quantity):
    """
    Insert a meal into the database.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO meals
        (
            food_name,
            meal_type,
            calories,
            protein,
            fat,
            carbs,
            fiber,
            sugar,
            quantity
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        food_name,
        meal_type,
        calories,
        protein,
        fat,
        carbs,
        fiber,
        sugar,
        quantity
    ))

    conn.commit()
    conn.close()


def get_all_meals():
    """
    Fetch all meals.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM meals
        ORDER BY date DESC
    """)

    meals = cursor.fetchall()

    conn.close()

    return meals


def get_today_totals():
    """
    Calculate today's nutrition totals.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            COALESCE(SUM(calories),0) AS calories,
            COALESCE(SUM(protein),0) AS protein,
            COALESCE(SUM(fat),0) AS fat,
            COALESCE(SUM(carbs),0) AS carbs,
            COALESCE(SUM(fiber),0) AS fiber,
            COALESCE(SUM(sugar),0) AS sugar
        FROM meals
        WHERE DATE(date)=DATE('now')
    """)

    totals = cursor.fetchone()

    conn.close()

    return totals


def delete_meal(meal_id):
    """
    Delete a meal by ID.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM meals WHERE id=?",
        (meal_id,)
    )

    conn.commit()
    conn.close()