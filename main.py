from flask import Flask, jsonify , request

import json

app = Flask(__name__)


def has_three_same_letters(word_string):
    #print("Check if word_string have same 3 letters in a row for : "+word_string )
    for i in range(len(word_string) - 2):
        if word_string[i] == word_string[i+1] == word_string[i+2]:
            return True
    return False



def has_three_letters_in_order(word_string):
    word_string = word_string.lower()  # or word_string.upper()
    #print("Check if 3 letters are in alphabetical order : " + word_string)
    for i in range(len(word_string) - 2):
      #  print(ord(word_string[i]))
        if ord(word_string[i]) == ord(word_string[i+1]) - 1 == ord(word_string[i+2]) - 2:
            return True
    return False

@app.route('/sort-strings', methods=['POST'])
def sort_strings():
    # Get the input strings from the request
    # print(request.json['strings'])
    # print(request.json)
    input_strings = request.json['strings']
    print(input_strings)
    
    # # Sort the input strings
    sorted_strings = sorted(input_strings)
    res = False
    if has_three_letters_in_order(word_string = input_strings):
        res = True
    elif has_three_same_letters(word_string = input_strings):
        res = True
    else:
        res = False
    # Return the sorted strings in a JSON response
    response_data = { "result" : res}
    return jsonify(response_data)
    

if __name__ == '__main__':
    app.run()
