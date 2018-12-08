# Python word count program
# Date: 8 Dec, 2018
print("Python is opening files...");
f = open("//home//socialclimber//Desktop/Python//Chars_In_Word//text.txt","r");
f_out = open("//home//socialclimber//Desktop/Python//Chars_In_Word//text_wc.txt","w")
print("Done opening files");
# use a for loop to read the lines in the file
print("Now counting words in the file");
count = 0;
for line in f:
        # Split line into words
	tokens = line.split(" "); 
	nun_of_words = len(tokens);
	# accumulate the number of words in a count variable
	count = count+nun_of_words;
	# write the line an it's number of words to the file
	f_out.write(" Words: "+str(nun_of_words)+" "+line);
	# count characters in each word
	for word in tokens:
	        f_out.write(word+": has "+str(len(word))+" Characters\n");
#write total number of words in the file to the output file
f_out.write("total number of words in file: "+ str(count));
#close resource that were opened
print("Closing resources");
f.close();
f_out.close();
print("Done! Check your output file text_wc.txt")
	
	
