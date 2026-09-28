# content.py
# Handles quotes, jokes, and facts

import random


QUOTES = [
    "Believe in yourself and keep moving forward.",
    "Success comes from consistent effort.",
    "Every expert was once a beginner.",
    "Small progress is still progress.",
    "Don't stop until you are proud of yourself."
]


JOKES = [
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why was the Python programmer confused? Because he couldn't find the right indentation!",
    "What do computers eat for breakfast? Microchips!",
    "Why did the developer go broke? Because he used up all his cache!"
]


FACTS = [
    "Python was created by Guido van Rossum.",
    "The Earth takes about 365 days to orbit the Sun.",
    "Water covers about 71 percent of Earth's surface.",
    "The human brain contains billions of neurons.",
    "The speed of light is approximately 300,000 kilometers per second."
]


def get_random_quote():
    """Return a random motivational quote."""
    return random.choice(QUOTES)


def get_random_joke():
    """Return a random joke."""
    return random.choice(JOKES)


def get_random_fact():
    """Return a random fact."""
    return random.choice(FACTS)