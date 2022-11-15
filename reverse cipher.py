message = 'This is program to explain reverse cipher.'
translated = '' #cipher text is stored in this variable
j = len(message) - 1

while i >= 0:
   translated = translated + message[j]
   j = j - 1
print(“The cipher text is : “, translated)
