# 🥗 AI Nutrition Analyzer & Daily Diet Tracker

A Flask-based web application that analyzes food nutrition using the **USDA FoodData Central API**. Users can search for food items, view detailed nutritional information, save meals to a daily tracker, monitor nutrition intake, and receive AI-inspired dietary recommendations.

---

## 📌 Features

* 🔍 Search food items using the USDA FoodData Central API
* 🔥 View calories and nutritional information
* 💪 Display protein, fat, carbohydrates, fiber, and sugar
* 🍽️ Add meals to a daily nutrition tracker
* 📊 Dashboard with nutrition summary and charts
* 🤖 AI-inspired health recommendations based on daily intake
* 💾 SQLite database for storing meal history
* 🌐 Responsive web interface built with Flask

---

## 🛠️ Technologies Used

### Frontend

* HTML5
* CSS3
* JavaScript
* Chart.js

### Backend

* Python
* Flask

### Database

* SQLite

### API

* USDA FoodData Central API

### Python Libraries

* Flask
* Requests
* python-dotenv

---

## 📁 Project Structure

```text
Nutrition-Analyzer/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
├── .env
├── database.db
│
├── models/
│   └── database.py
│
├── services/
│   └── usda_api.py
│
├── utils/
│   └── recommendation.py
│
├── templates/
│   ├── index.html
│   ├── tracker.html
│   └── dashboard.html
│
└── static/
    ├── style.css
    ├── script.js
    └── images/
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Nutrition-Analyzer.git
```

### 2. Open the project

```bash
cd Nutrition-Analyzer
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Create a `.env` file

```text
USDA_API_KEY=YOUR_API_KEY
```

### 7. Run the application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## 📷 Application Modules

* Home Page
* Food Search
* Nutrition Analysis
* Daily Meal Tracker
* Nutrition Dashboard
* AI Health Recommendations

---

## 📊 Database

The application automatically creates an SQLite database (`database.db`) to store:

* Food Name
* Meal Type
* Calories
* Protein
* Fat
* Carbohydrates
* Fiber
* Sugar
* Quantity
* Date & Time

---

## 🤖 AI Recommendation Logic

The application analyzes the user's daily nutritional intake and provides health recommendations such as:

* High calorie alerts
* Low protein suggestions
* High fat warnings
* High carbohydrate alerts
* Fiber improvement tips
* Sugar intake warnings

---

## 🎯 Future Enhancements

* User authentication
* Weekly and monthly nutrition reports
* PDF report generation
* Food image integration
* BMI calculator
* Water intake tracker
* Personalized nutrition goals

---

## 👩‍💻 Developed By

**Samriddhi Gupta**

AI/ML Internship Final Project

---

## 📄 License

This project is developed for educational and internship purposes.
