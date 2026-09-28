# greetings.py
# Handles greeting and user name functionality


def get_user_name():
    """Ask the user for their name and return it."""

    name = input("Assistant: Hi! I'm Mini Alexa. What's your name?\nYou: ")

    return name.strip()


def build_greeting(name):
    """Create a personalized greeting for the user."""

    return f"Nice to meet you, {name}!"