from flask import Flask, request, jsonify
# import nltk
# import random
# import string
# import pandas as pd
# import demochat

from demochat import response
from demochat import greeting

app = Flask(__name__)
@app.route('/<chat>/', methods=['GET','POST'])


def response(user_response):
    flag = True
    return "ROBO: My name is Robo. I will answer your queries about Chatbots. If you want to exit or dont find me useful, type Bye!"
    while (flag == True):
        user_response = input()
        user_response = user_response.lower()
        if (user_response != 'bye'):
            if (user_response == 'thanks' or user_response == 'thank you'):
                flag = False
                return "ROBO: You are welcome.."
            else:
                if (greeting(user_response) != None):
                    return ("ROBO: " + greeting(user_response))
                else:
                    print("ROBO: ", end=" ")
                    print(response(user_response))
                    sent_tokens.remove(user_response)
        else:
            flag = False
            return "ROBO: Bye! take care.."
        # p=response(user_response='')
        # return p

if __name__ == '__main__':
    app.run(host="localhost", port=7070, debug=True)
