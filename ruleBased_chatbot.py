def chatbot_response(user_input):
    # Define a dictionary with predefined keywords and responses
    responses = {
        "hello": "Hi there! How can I help you?",
        "hi": "Hello! What can I do for you today?",
        "how are you": "I'm just a chatbot, but I'm doing great! How about you?",
        "bye": "Goodbye! Have a great day!",
        "thanks": "You're welcome!",
        "help": "Sure! How can I assist you?"
    }
    
    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower()
    
    # Find the appropriate response
    for keyword in responses:
        if keyword in user_input:
            return responses[keyword]
    
    # Default response if no keyword matches
    return "I'm sorry, I don't understand that."

def main():
    print("Welcome to the Simple Chatbot! Type 'exit' to end the conversation.")
    
    while True:
        # Get user input
        user_input = input("You: ")
        
        # Exit the chatbot
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        
        # Get the chatbot's response
        response = chatbot_response(user_input)
        
        # Print the chatbot's response
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
