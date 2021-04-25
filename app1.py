import json
from difflib import get_close_matches

data = json.load(open("C:/Users/pc/Desktop/Python Projects/Applications/Application 1/data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if Yes, or N if No : " %get_close_matches(word,data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word,data.keys())[0]]
        elif yn == "N":
            return "The Word doesn't exists. Please double check it."
        else:
            return "We didn't understand your entry"
    else:
        return "The Word doesn't exists. Please double check it."

word = input("Enter word : ")
output = translate(word)

if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)