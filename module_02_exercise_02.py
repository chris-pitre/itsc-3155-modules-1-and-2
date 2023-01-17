userString = input("Enter a string: ")
userString = [*userString]

rearrangedString = [i for i in userString if i.islower()]
rearrangedString.extend([i for i in userString if i.isupper()])
rearrangedString = "".join(rearrangedString)

print(rearrangedString)