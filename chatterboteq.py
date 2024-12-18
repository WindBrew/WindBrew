print("Chatbot: Hello there, type 'quit' to exit")
responses = {
    "hi" : "Hello, how can I assist you today?",
    "hello" : "Hi, how can I assist you today?",
    "how are you" : "Just a basic chatbot pew pew",
    "what is your name" : "My name is 'A' chatbot",
    "goodbye" : "it was nice meeting you ____",
    "bye" : "it was nice meeting you stranger, have a good day",
    
}
while True :
    user_inp = (input("You: ")).lower()
    if user_inp.lower() == "quit":
         confirm = input("do you really want to quit?, [reply with (yes,no)]:\n")
         if confirm.strip().lower() == "yes":
             print("Chatbot: Goodbye, it was nice communicating with you")
             break
            
        
         else:
              print("Oh, sure let's continue")
              continue
         
    else:
         if user_inp in responses :
             print(f"Chatbot:{responses.get(user_inp)}")
         else:
             print("Chatbot: Thats..., out of my processing capability sorry!!!")
