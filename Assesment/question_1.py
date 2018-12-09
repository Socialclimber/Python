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
	for msg in f:
		#msg = line
		for i in range(len(msg)):
			if ord(msg[i]) == 32: #check if char is a space
				#print(msg[i])
				dct_msg += chr(ord(msg[i])) # cocncatenate back our text, space not  encrypted
			elif (ord(msg[i]) == 39 or ord(msg[i]) == 40 or ord(msg[i]) == 41 or ord(msg[i]) == 46):
				dct_msg += chr(ord(msg[i]))

			elif (ord(msg[i]) - key > 90) and (ord(msg[i]) - key < 97):
				# move back to 'A' after 'Z'
				temp = (ord(msg[i]) - key) + 26
				dct_msg += chr(temp)
				
			elif (ord(msg[i]) - key) < 65:
				temp = (ord(msg[i]) - key) + 26
				dct_msg += chr(temp)
			elif (ord(msg[i]) == 10):
				dct_msg += chr(ord(msg[i]))
				
			else:
				# in case of letters a-z and A-Z
				dct_msg += chr(ord(msg[i]) - key)
	f_out.write(dct_msg);
	print("Done decripting file, check message in decrypted_fil.txt!")
	f.close()
	f_out.close()

# call the decryption method on the file
decryption()