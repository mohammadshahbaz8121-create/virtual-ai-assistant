# main.py
# Main entry point for Mini Alexa

from ai_concepts import recommend_activity, perceptron_demo
from content import get_random_quote, get_random_joke, get_random_fact
from datetime_utils import get_current_date, get_current_time
from calculator import parse_expression, calculate
from greetings import get_user_name, build_greeting
from game import play_guessing_game


def main():

    print("=" * 50)
    print("        MINI ALEXA - VIRTUAL AI ASSISTANT")
    print("=" * 50)

    name = get_user_name()

    print(f"\nAssistant: {build_greeting(name)}")
    print("Assistant: Type 'help' to see what I can do.")

    while True:

        command = input(f"\n{name}: ").lower().strip()

        # Greetings
        if command in [
            "hello",
            "hi",
            "hey",
            "good morning",
            "good afternoon",
            "good evening"
        ]:

            if command == "good morning":
                print(f"Assistant: Good morning, {name}!")

            elif command == "good afternoon":
                print(f"Assistant: Good afternoon, {name}!")

            elif command == "good evening":
                print(f"Assistant: Good evening, {name}!")

            else:
                print(f"Assistant: Hello, {name}! How can I help you?")

        # Help
        elif command == "help":

            print("\nAssistant: I can help you with:")
            print("- hello / hi / hey")
            print("- time")
            print("- date")
            print("- calculate")
            print("- joke")
            print("- quote")
            print("- fact")
            print("- game")
            print("- recommend")
            print("- perceptron")
            print("- exit")

        # Time
        elif (
            command == "time"
            or "what is the time" in command
            or "tell me the time" in command
            or "current time" in command
        ):

            print(f"Assistant: The current time is {get_current_time()}.")

        # Date
        elif (
            command == "date"
            or "what is today's date" in command
            or "what is the date" in command
            or "tell me the date" in command
            or "today's date" in command
        ):

            print(f"Assistant: Today's date is {get_current_date()}.")

        # Calculator
        elif command == "calculate":

            expression = input(
                "Assistant: Enter calculation (example: 10 + 5): "
            )

            try:
                first_number, operator, second_number = parse_expression(expression)

                result = calculate(
                    first_number,
                    operator,
                    second_number
                )

                print(f"Assistant: The answer is {result}")

            except ValueError as error:
                print(f"Assistant: {error}")

            except ZeroDivisionError as error:
                print(f"Assistant: {error}")

        # Joke
        elif (
            command == "joke"
            or "tell me a joke" in command
            or "make me laugh" in command
            or "say a joke" in command
        ):

            print(f"Assistant: {get_random_joke()}")

        # Quote
        elif (
            command == "quote"
            or "give me a quote" in command
            or "tell me a quote" in command
            or "motivate me" in command
        ):

            print(f"Assistant: {get_random_quote()}")

        # Fact
        elif (
            command == "fact"
            or "tell me a fact" in command
            or "give me a fact" in command
            or "interesting fact" in command
        ):

            print(f"Assistant: {get_random_fact()}")

        # Guessing game
        elif (
            command == "game"
            or "play a game" in command
            or "guessing game" in command
        ):

            play_guessing_game()

        # Recommendation
        elif (
            command == "recommend"
            or "recommend something" in command
            or "what should i do" in command
        ):

            print(f"Assistant: {recommend_activity()}")

        # Perceptron
        elif command == "perceptron":

            try:
                input_1 = float(
                    input("Assistant: Enter first input: ")
                )

                input_2 = float(
                    input("Assistant: Enter second input: ")
                )

                result = perceptron_demo(input_1, input_2)

                print(f"Assistant: Perceptron output is {result}")

            except ValueError:
                print("Assistant: Please enter valid numbers.")

        # Exit
        elif command in ["exit", "quit", "bye"]:

            print(f"\nAssistant: Goodbye, {name}! Have a great day.")
            break

        # Unknown command
        else:

            print("Assistant:   Sorry, I don't understand that command.")
            print("Assistant: Type 'help' to see the available commands.")


if __name__ == "__main__":
    main()