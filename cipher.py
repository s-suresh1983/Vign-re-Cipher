# get position in alphabet for a letter
def calculate_shifts(letter):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    position = alphabet.index(letter)
    return position

# shifts letter in alphabet by "key" positions, if resulted position is bigger
# than alphabet starts again at the beginning of the alphabet
def encrypt_letter(character, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if character.isalpha(): 
        initialPosition = calculate_shifts(character)
        finalPosition = initialPosition + key
        if finalPosition >= len(alphabet):   #end of alphabet reached
            finalPosition = finalPosition - len(alphabet)
        return alphabet[finalPosition]
    return character


def encrypt_text(text, keyword):
    text = text.lower()
    keyword = keyword.lower()
    keywordLength = len(keyword)
    counter = 0
    encryptedtext = ""
    for character in text:
        if counter >= keywordLength:
            counter = 0
        key = calculate_shifts(keyword[counter])
        encryptedletter = encrypt_letter(character, key)
        encryptedtext = encryptedtext + encryptedletter
        counter = counter + 1
    return encryptedtext    


input_text = input("Which text should be encrypted: ")
input_keyword = input("Which keyword should be used? ")
print(encrypt_text(input_text, input_keyword))
