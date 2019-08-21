######## Functions and Global Variables ###################1
def hacker(text):
    for ch in ['a', 'e', 'i', 'o', 'u', 's']:
        if ch in text:
            text = text.replace('a', '4').replace('e', '3').replace('i', '1').replace('o', '0').replace('u', 'V').replace('s', '$')
    return text

text = input("Type in a sentence and we'll l33t-i-fy it for you: ")
###########################################################1

############# User Commands ###############################2
print (hacker(text))
###########################################################2
