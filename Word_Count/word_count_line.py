f = open("//home//socialclimber//Desktop/Python//Word_Count//text.txt");

# use a for loop to read the lines in the file
count = 0;
for line in f:
	tokens = line.split(" ");
	print(line)
	print(" Words: ")
	print(len(tokens));
	count+=len(tokens);
print("Total Words in file: ")
print(count);
	
	
