"""
CodeAlpha_Chatbot
Task 4: Basic Chatbot
A simple rule-based chatbot that replies to predefined user inputs.
"""

import random


def get_response(user_input):
    text = user_input.lower().strip()

    # Greetings
    if text in ["hello", "hi", "hey"]:
        return "Hi!"

    # Wellbeing check
    elif "how are you" in text:
        return "I'm fine, thanks!"

    # Farewell
    elif text in ["bye", "goodbye", "see you"]:
        return "Goodbye!"

    # Name questions
    elif "your name" in text:
        return "I'm CodeBot, your friendly assistant!"

    # Thanks
    elif "thank" in text:
        return "You're welcome!"

    # Help
    elif "help" in text:
        return "I can chat about simple things. Try saying hello, asking how I am, or saying bye!"

    # What can you do
    elif "what can you do" in text:
        return "I'm a simple rule-based chatbot. I can respond to greetings, basic questions, and farewells."

    # Time-related small talk
    elif "what time" in text or "time is it" in text:
        return "I don't have a clock, but I'm always here to chat!"

    # Weather small talk
    elif "weather" in text:
        return "I can't check the weather, but I hope it's nice where you are!"

    # Compliment
    elif "good bot" in text or "you are smart" in text or "you're smart" in text:
        return "Aww, thank you! You're pretty great yourself."

    # Joke request
    elif "joke" in text:
        return random.choice([
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "Why did the computer go to therapy? It had too many unresolved issues.",
            "I told a chatbot a joke once. It crashed laughing... literally."
        ])

    # Fallback for anything unrecognized
    else:
        return "Sorry, I didn't understand that. Could you rephrase?"


def chat():
    print("Chatbot: Hi! I'm a simple chatbot. Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("Chatbot:", response)

        if user_input.lower().strip() in ["bye", "goodbye", "see you"]:
            break


if __name__ == "__main__":
    chat()
