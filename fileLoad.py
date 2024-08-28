import random

def fileload():
    quote=[]
    with open("motivationalquote.txt") as quotes:
        for line in quotes:
            quote.append(line.strip())

    todays_quote=quote[random.randint(0,len(quote))]
    return todays_quote


