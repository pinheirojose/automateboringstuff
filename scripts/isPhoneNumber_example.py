def isPhoneNumber(text):
    if len(text) != 12:
        return False #not a phone number
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False #no area code
        if text[3] != '-':
            return False #missing dash
        for i in range(4,7):
            if not text[i].isdecimal():
                return False
        if text[7] != '-':
            return False #missing second dash
        for i in range(8,12):
            if not text[i].isdecimal():
                return False
        return True

message = 'Call me 415-555-1001, or at 415-555-9999'
foundNumber = False

for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
        foundNumber = True
if not foundNumber:
    print('No phones found')
