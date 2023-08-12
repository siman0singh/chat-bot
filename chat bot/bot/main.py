from chat021.chat import chat_conversation
from chat021.learn import learn 

def main():
    chat_conversation.greeting()
    while True:
        data = input(f'Siman: ')
        learn(data)
    

if __name__ == "__main__":
    main()