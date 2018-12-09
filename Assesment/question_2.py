# program to find characters in a mess
import re
f = open("//home//socialclimber//Desktop//Assesment//mess.txt","r");
data = f.read()
count = {}
characters = ""
string = "abcdefghijklmnopqrstuvwxyzQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
for c in data:
	count[c] = count.get(c, 0)+1

for s in string:
	if s in count.keys():
		characters = characters + s + ", "
print(characters)