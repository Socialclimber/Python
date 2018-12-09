def encryption():
	print("Encription Function")
	print("Message can only be lower or uppercase letters")
	msg = input("Enter message:")
	key = int(input("Eneter key(0-25): "))
	encrypted_text = ""
	for i in range(len(msg)):
		if ord(msg[i]) == 32: #check if char is a space
			encrypted_text += chr(ord(msg[i])) # cocncatenate back our text, space not  encrypted
		elif ord(msg[i]) + key > 122:
			# after 'z' move back to 'a', 'a' = 97, 'z' = 122
			temp = (ord(msg[i])+ key) - 122 # this will return a lower int
			# we can now add 96 to tempt and convert it back to a char
			encrypted_text += chr(96 + temp)
		elif (ord(msg[i]) + key > 90) and (ord(msg[i]) <= 96):
			# move back to 'A' after 'Z'
			temp = (ord(msg[i]) + key) - 90
			encrypted_text += chr(64+temp)
		else:
			# in case of letters a-z and A-Z
			encrypted_text += chr(ord(msg[i]) + key)
	print("Encripted Text: "+ encrypted_text);
encryption()
