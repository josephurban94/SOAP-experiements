import zeep
wsdl_url = 'http://localhost:1337/soap-service?wsdl'
client = zeep.Client(wsdl=wsdl_url)

userInput = input("Enter an ascii string to encrypt: ")
output = client.service.toCipher(userInput)
print("The encrypted text is:\n", output)
output = client.service.fromCipher(output)
print("The original text was:\n", output)

userInput = input("Enter a string to decrypt: ")
output = client.service.fromCipher(userInput)
print("The original text was:\n", output)

userInput = input("Enter an integer: ")
userInput2 = input("Enter a second integer to add to the original: ")
output = client.service.add(userInput,userInput2)
print("The value of the integers summed is:\n", output)

userInput = input("Enter an integer: ")
userInput2 = input("Enter a second integer to subtract from the original: ")
output = client.service.sub(userInput,userInput2)
print("The value of the second integer subtracted from the first is:\n", output)

