from fuzzywuzzy import fuzz

# Define the pre-defined responses
predefined_responses = {
    "Hello": "Hi",
    "What are you?": "I'm the future",
    "Can you do math": "No I'm too dumb to do Math"
}

# Define the function that responds to the user's message
def respond(message):
    # Check if the user's input is close to one of the pre-defined inputs
    for predefined_message in predefined_responses:
        similarity = fuzz.ratio(message.lower(), predefined_message.lower())
        if similarity > 70:
            return predefined_responses[predefined_message]
    return "I don't understand what you're saying."

# Ask for the user's input and respond with the chatbot's message
while True:
    user_message = input("You: ")
    chatbot_message = respond(user_message)
    print("Chatbot:", chatbot_message)
