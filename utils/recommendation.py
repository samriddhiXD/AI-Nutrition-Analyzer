def generate_recommendation(calories, protein, fat, carbs, fiber, sugar):
    """
    Generate nutrition recommendations based on daily intake.
    """

    recommendations = []

    # Calories
    if calories > 2500:
        recommendations.append(
            "⚠️ Your calorie intake is high. Try reducing fried and sugary foods."
        )
    elif calories < 1500:
        recommendations.append(
            "🍽️ Your calorie intake is low. Consider eating balanced meals."
        )

    # Protein
    if protein < 50:
        recommendations.append(
            "🥚 Increase protein intake by eating eggs, paneer, tofu, chicken, fish, or lentils."
        )

    # Fat
    if fat > 70:
        recommendations.append(
            "🥑 Your fat intake is high. Choose healthier fats and reduce processed food."
        )

    # Carbohydrates
    if carbs > 300:
        recommendations.append(
            "🍚 High carbohydrate intake detected. Include more vegetables and whole grains."
        )

    # Fiber
    if fiber < 25:
        recommendations.append(
            "🥗 Increase fiber by eating fruits, vegetables, oats, and whole grains."
        )

    # Sugar
    if sugar > 50:
        recommendations.append(
            "🍬 Your sugar intake is high. Reduce soft drinks, sweets, and packaged snacks."
        )

    # Healthy
    if len(recommendations) == 0:
        recommendations.append(
            "✅ Excellent! Your nutrition intake looks balanced. Keep maintaining a healthy lifestyle."
        )

    return recommendations