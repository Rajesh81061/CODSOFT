def simple_chatbot():
    print("Hello! I'm your simple chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").strip().lower()
        
        if user_input == 'bye':
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        elif 'hello' in user_input or 'hi' in user_input:
            print("Chatbot: Hello! How can I help you today?")
        
        elif 'how are you' in user_input:
            print("Chatbot: I'm just a bot, but I'm doing great! How about you?")
        
        elif 'your name' in user_input:
            print("Chatbot: I'm a simple chatbot created to assist you.")
        
        elif 'time' in user_input:
            from datetime import datetime
            current_time = datetime.now().strftime("%H:%M:%S")
            print(f"Chatbot: The current time is {current_time}.")
        
        elif 'date' in user_input:
            from datetime import datetime
            current_date = datetime.now().strftime("%Y-%m-%d")
            print(f"Chatbot: Today's date is {current_date}.")
            
        elif '"I forgot my password, can you help me reset it?"' in user_input:
                print("Chatbot: yes please provide your email address.. we will send reset link")
                
        elif '"What products do you offer?"' in user_input:
                    print("Chatbot: we offer a wide range of products starting from day to day household items to electronic items.")
                    
        elif '"How do I order a product?"' in user_input:
                        print("Chatbot: simple! just go to the homepage and and click the options tab and click on order items tab")
                        
        elif '"How do I create an account?"' in user_input:
                            print("Chatbot: it'simple! just go to the website homepage and click on signup or create an account on top right side corner where it asks to enter email address or phone number and then you can click on submit and enter OTP number..thats it!there you go.")
                                 
        elif 'thank you' in user_input or 'thanks' in user_input:
            print("Chatbot: You're welcome!")
        
        else:
            print("Chatbot: I'm sorry, I didn't understand that. Can you please rephrase?")

if __name__ == "__main__":
    simple_chatbot()