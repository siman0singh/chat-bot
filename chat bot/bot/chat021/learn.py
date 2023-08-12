
from chat021.chat import chat_conversation as chat
def learn(data):

    if "day" in data:
        chat.day()

    elif "news" in data:
        chat.news()

    elif "time" in data:
        chat.current_time()

    elif "temp" in data:
        chat.temp()

    elif "plans" in data:
        chat.plans()

    elif "breakfast" in data:
        chat.breakfast()
    

    elif "exit" in data:
        chat.Exit()

    else:
        print(" Sorry,I don't know the answer")   
