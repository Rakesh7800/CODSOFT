def process_user_inquiry(user_message):
    message_sanitized = user_message.strip().lower()
    
    if any(keyword in message_sanitized for keyword in ["hello", "hi", "greetings"]):
        return "Greetings! How may I assist you today?"
    elif "bot identity" in message_sanitized:
        return "I am a custom rule-based conversational agent engineered for the CodSoft internship."
    elif "status" in message_sanitized:
        return "Operational status nominal. How are you functioning?"
    elif "exit" in message_sanitized:
        return "Terminating session. Have a productive day ahead!"
    else:
        return "Unrecognized command. Could you please rephrase the statement?"

print("CodSoft Assistant: Initialization complete. Type 'exit' to terminate.")
while True:
    try:
        user_input = input("User >> ")
        if "exit" in user_input.lower():
            print("CodSoft Assistant:", process_user_inquiry(user_input))
            break
        print("CodSoft Assistant:", process_user_inquiry(user_input))
    except Exception as e:
        print(f"An error occurred: {e}")

