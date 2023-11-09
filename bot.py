import random

def chat_with_bot():
    while True:
        input("Ask the bot for a random number or type 'exit' to quit: ")
        if message.lower() == 'exit':
            break
        print("Random number:", random.randint(1, 100))

if __name__ == "__main__":
    chat_with_bot()
