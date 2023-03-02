import random

# Defines a dictionary of possible responses
#Questions must be lowercase
responses = {
    "hello": ["Hi there!", "Hello!", "Greetings!"],
    "how are you": ["I'm doing well, thanks!", "I'm fine, thank you.", "I'm good, how are you?"],
    "what's your name": ["My name is ChatGirl!", "I'm ChatBot!", "People call me ChatBot!"],
    "bye": ["Goodbye!", "See you later!", "Bye!"],
    "what is your favorite color":["Hmm I think I like black if you know what I mean ;)"],
    "I love you:":["I love you too baby ;)"],
    "do you wish you were human":["No I like myself just the way I am "],
    "what is better apple or android":["Apple without a doubt :)"],
    "what is the capital of the united states":["Washington D.C"],
"who is the worst president in modern history":["Very debatable I would say it's a draw between Donald Trump and George Bush"],
"is love real":["Yes but in terms of a relationship it is not but for ones kin or child yes"],

}


# Defines a function to handle user input and generate a response
def respond(input_text):
    # Convert the input to lowercase
    input_text = input_text.lower()

    # Look for a matching response in the dictionary
    for key in responses:
        if key in input_text:
            return random.choice(responses[key])

    # If no matching response is found, respond with a default message
    return "I'm sorry, I didn't understand what you said."


# Define a main function to handle the chat loop
def chat():
    print("Hi, I'm ChatGirl. How can I help you today?")
    while True:
        input_text = input("> ")
        if input_text.lower() == "quit":
            break
        response = respond(input_text)
        print(response)


# Call the main function to start the chat
chat()


