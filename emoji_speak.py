import pyperclip
print("This program converts normal text to emoji text in discord.")
print("YOU CAN ONLY USE A-Z!")
strin = input("Sentance to emoji-fy: ") #Get text
strin = strin.lower() #Format the text
emojis = "" #Declare the output array
numbdict = {
    48 : 'zero',
    49 : 'one',
    50 : 'two',
    51 : 'three',
    52 : 'four',
    53 : 'five',
    54 : 'six',
    55 : 'seven',
    56 : 'eight',
    57 : 'nine',
}

part1 = ":regional_indicator_"
part2 = ": "
spce = "    "
newvar = 0 #Initialize the loop
while(newvar < len(strin)):
    if(ord(strin[newvar]) == 32):
        emojis = emojis + spce
    elif(ord(strin[newvar]) > 47 and ord(strin[newvar]) < 58):
        emojis = emojis + " :"
        emojis = emojis + numbdict[ord(strin[newvar])]
        emojis = emojis + ": "
    elif(ord(strin[newvar]) == 39):
        emojis = emojis + " ' "
    elif(ord(strin[newvar]) == 33):
        emojis = emojis + ":exclamation:"
    elif(ord(strin[newvar]) == 44):
        emojis = emojis + " , "
    elif(ord(strin[newvar]) == 46):
        emojis = emojis + " . "
    elif(ord(strin[newvar]) == 58):
        emojis = emojis + " : "
    elif(ord(strin[newvar]) == 63):
        emojis = emojis + ":question:"
    else:
        outpt = part1 + strin[newvar] + part2
        emojis = emojis + outpt
    newvar += 1
print("\n")
print(emojis)
try:
    pyperclip.copy(emojis)
except:
    print("\nSorry kiddo, gonna have to copy the above yourself.")
