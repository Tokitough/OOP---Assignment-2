#ask user for input
print("\u001b[30m=" * 70)
input = input("\u001b[32mInput a string to decrypt: ")
output = ""

# check characters
for i in range(len(input)):
# change '*' = a
    if input[i] == "*":
        output += "a"
# change '&' = e
    elif input[i] == "&":
        output += "e"
# change '#' = i
    elif input[i] == "#":
        output += "i"
# change '+' = o 
    elif input[i] == "+":
        output += "o"
# change '!' = u
    elif input[i] == "!":
        output += "u"
    else:
        output += input[i]

# print output
print("\u001b[30m=" * 70)
print("\u001b[34mThe decrypted input is: " + output)
print("\u001b[30m=" * 70)
