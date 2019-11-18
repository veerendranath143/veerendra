from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os


bot=ChatBot("bot")
bot=ListTrainer(bot)
for files in os.listdir("C:/Users/naruk/OneDrive/Desktop/ammu/chatterbot-corpus-master/chatterbot-corpus-master/chatterbot_corpus/data/english/"):
    data=open("C:/Users/naruk/OneDrive/Desktop/ammu/chatterbot-corpus-master/chatterbot-corpus-master/chatterbot_corpus/data/english/")
    bot.train(data)
while True:
    msg=input("you:")
    reply=bot.get_response(msg)
    print("bot:",reply)
    if msg.strip()== 'bye':
        print("bye")
        break