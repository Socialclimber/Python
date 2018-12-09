# Let's implement the decryption function
# key
# K ­- M
# O ­- Q
# E ­- G
# From the key above, it shows that ordinal of the key is 2 since each character
# These can be determined by ord(M) - ord(K)
def decryption():
	# create the file object
	f = open("//home//socialclimber//Desktop//Assesment//cyphertext","r");
	f_out = open("//home//socialclimber//Desktop//Assesment//decripted_file","w");
	
	# Let's get the key value
	key = ord('M') - ord('K') 

	# define a string variable to store the decripted message
	dct_msg = ""

	# read the content of the file on line at a time
	for line in f:
		for c in line:
			if c >= 'a' and c <= 'z':
				dct_msg += chr(((ord(c) + 2) - ord('a'))%26 + ord('a'))
			else:
				dct_msg += c
	f_out.write(dct_msg);
	print("Done decripting file, check message in decrypted_fil.txt!")
	f.close()
	f_out.close()

# call the decryption method on the file
decryption()