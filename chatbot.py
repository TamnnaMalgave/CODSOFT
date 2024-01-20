
def simple_chatbot(ip):
    ip = ip.lower()

    if "hello" in ip:
        return "Hi there! How can I help you today?"

    elif "how are you" in ip:
        return "I'm just a chatbot, but thanks for asking!"

    elif "goodbye" in ip or "bye" in ip:
        return "Goodbye! Have a great day!"

    elif "name" in ip:
        return "I am a simple chatbot."

    else:
        return "I'm sorry, I didn't understand that."

while True:
    ip = input("You: ")
    
   
    if "goodbye" in ip or "bye" in ip:
        print("Chatbot: Goodbye!")
        break

    response = simple_chatbot(ip)
    print("Chatbot:", response)
