# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

letter_num = {}
text_key = {}
hiddin_messige = ""

with open("ciphertext.txt", encoding="utf-8") as encoded:
    text = encoded.read()

change = [
'E',
'T', 
'A', 
'O', 
'H', 
'N', 
'R', 
'I', 
'S', 
'D', 
'L', 
'W', 
'U',
'G', 
'F', 
'B', 
'M', 
'Y', 
'C', 
'P', 
'K', 
'V', 
'Q', 
'J', 
'X', 
'Z']

for letter in text:

    if letter.isalpha():

        if letter not in letter_num:
            letter_num[letter] = 1
        else:
            letter_num[letter] += 1

sort_text = list(letter_num.items())
sort_text.sort(reverse=True, key=lambda item: item[1])

for index, letter in enumerate(change):

    text_key[sort_text[index][0]] = change[index]

for letter in text:

    if letter.isalpha():
        hiddin_messige = hiddin_messige + text_key[letter]
    else:
        hiddin_messige = hiddin_messige + letter

print(hiddin_messige)