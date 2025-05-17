def analyze_message(message):
    message = message.lower()

    if "hello" in message or "hi" in message:
        return "Hello! How can I assist you today?"
    elif "help" in message or "support" in message:
        return "Sure, I can help. Please describe your issue."
    elif "bye" in message:
        return "Goodbye! Have a great day."
    else:
        return "I'm not sure how to respond to that. Can you rephrase?"

