# ai_concepts.py
# Demonstrates simple AI and ML concepts


def recommend_activity():
    """Recommend an activity based on the current time."""

    from datetime import datetime

    current_hour = datetime.now().hour

    if current_hour < 12:
        return "Good morning! You could start your day with some learning."

    elif current_hour < 17:
        return "It's afternoon! You could work on a coding project."

    else:
        return "It's evening! You could review what you learned today."


def perceptron_demo(input_1, input_2):
    """Demonstrate a simple perceptron using fixed weights and bias."""

    weight_1 = 0.5
    weight_2 = 0.5
    bias = -0.5

    weighted_sum = (
        input_1 * weight_1
        + input_2 * weight_2
        + bias
    )

    if weighted_sum >= 0:
        output = 1
    else:
        output = 0

    return output