import os
import sys
import google.generativeai as palm

def ask_palm(question):
    palm.configure(api_key=os.environ["PALM_API_KEY"])
    response = palm.chat(messages=[question])
    return response.last

def main():
    while True:
        question = input("You: ")
        if question.lower() == "exit":
            break
        response = ask_palm(question)
        print("Bot: ", response)

if __name__ == "__main__":
    main()