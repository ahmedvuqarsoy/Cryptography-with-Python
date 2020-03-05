
def encryption(plaintext):
	return plaintext[::-1]

def decryption(ciphertext):
	return ciphertext[::-1]



def main():

	command = int(input("""
	_____Reverse Cipher_____
	=== CLICK
	= 1. For Encryption =
	= 2. For Decryption =
	
	Your Command: 	
	"""))

	text = input("Please, enter the string: ")

	if(command == 1):
		print(encryption(text))
	elif(command == 2):
		print(decryption(text))
	else:
		print("Unvalid command.")
		exit(1)

if __name__ == "__main__":
	main()
