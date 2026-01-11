# Simple Rule-Based Chatbot

print("Hello! I am a simple rule-based AI. Type 'quit' to exit.")

while True:
    user_input = input("You: ").lower()

    if user_input == "quit":
        print("Goodbye!")
        break
    elif "hello" in user_input:
        print("AI: Hello there!")
    elif "how are you" in user_input:
        print("AI: I am a program, so always good!")
    elif "name" in user_input:
        print("AI: I am RuleBot.")
    else:
        print("AI: Sorry, I don't understand.")
