import string

def chatbot():
    print("Bot: Hello! I'm a simple chatbot. Type 'bye' to exit.")
    responses = {
        "hello": "Hi!",
        "hi": "Hello!",
        "hey": "Hey there!",
        "tell me something about yourself": "I'm a simple rule-based chatbot, created using Python.",
        "who are you": "I'm a chatbot created using Python.",
        "help": "You can say hello, ask how I am, or type bye to exit.",
        "bye": "Goodbye!",
        "thank you": "You're welcome!",
        "thanks": "Happy to help!"
    }

    asked_how_user_is = False

    while True:
        user_input = input("You: ").lower().strip()
        user_input = user_input.translate(
            str.maketrans("", "", string.punctuation)
        )

        if user_input == "how are you":
            print("Bot: I'm fine, thanks! How are you?")
            asked_how_user_is = True
        elif asked_how_user_is and user_input in [
            "fine", "good", "i am fine", "i am good"
        ]:
            print("Bot: Glad to hear that!")
            asked_how_user_is = False
        elif asked_how_user_is and user_input in [
            "not good", "bad", "sad", "i am not fine"
        ]:
            print("Bot: I'm sorry to hear that. I hope things get better soon.")
            asked_how_user_is = False
        elif user_input in responses:
            print("Bot:", responses[user_input])
            if user_input == "bye":
                break
        else:
            print("Bot: I don't understand that. Try 'hello', 'help', or 'bye'.")

chatbot()
