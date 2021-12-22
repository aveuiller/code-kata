MORSE_CODE = {'.-...': '&', '--..--': ',', '....-': '4', '.....': '5', '...---...': 'SOS', '-...': 'B', '-..-': 'X', '.-.': 'R', '.--': 'W', '..---': '2', '.-': 'A', '..': 'I', '..-.': 'F', '.': 'E', '.-..': 'L', '...': 'S', '..-': 'U', '..--..': '?', '.----': '1', '-.-': 'K', '-..': 'D', '-....': '6', '-...-': '=', '---': 'O', '.--.': 'P', '.-.-.-': '.', '--': 'M', '-.': 'N', '....': 'H', '.----.': "'", '...-': 'V', '--...': '7', '-.-.-.': ';', '-....-': '-', '..--.-': '_', '-.--.-': ')', '-.-.--': '!', '--.': 'G', '--.-': 'Q', '--..': 'Z', '-..-.': '/', '.-.-.': '+', '-.-.': 'C', '---...': ':', '-.--': 'Y', '-': 'T', '.--.-.': '@', '...-..-': '$', '.---': 'J', '-----': '0', '----.': '9', '.-..-.': '"', '-.--.': '(', '---..': '8', '...--': '3'}

BIT_CODE = {"1":".", "111": "-", "0":"", "000": " ", "0000000": "   "}

def decodeBits(bits):
    bits = bits.strip("0")
    timeUnit = discoverTimeUnit(bits)
    mapping = dict((x*timeUnit, y) for x, y in BIT_CODE.items())
    items = sorted(mapping, key=len, reverse=True)
    for k in items: bits = bits.replace(k, mapping[k])
    return bits

def discoverTimeUnit(bits):
    timeUnit = inferBySpaces(bits)
    if timeUnit != -1: return timeUnit
    return inferByFirstSequence(bits)

def inferBySpaces(bits):
    index = bits.find("0000000")
    while index != -1:
        spaceStart = index
        spaceEnd = bits.find("1", spaceStart)
        if (spaceEnd - spaceStart) % 7 == 0: return (spaceEnd - spaceStart) / 7
        index = bits.find("0000000", spaceEnd)
    return -1

def inferByFirstSequence(bits):
    firstInput = bits.find("1")
    firstRelease = bits.find("0", firstInput) if bits.find("0", firstInput) != -1 else len(bits)
    secondInput = bits.find("1", firstRelease)
    
    inputLen = firstRelease - firstInput
    releaseLen =  secondInput - firstRelease if (secondInput - firstRelease) > 0 else 0 
    
    if inputLen % 3 == 0 and releaseLen % 3 != 0: inputLen = inputLen / 3
    return inputLen

def decodeMorse(morseCode):
    return ' '.join(decodeWord(word) for word in morseCode.split("   ")).strip().lstrip()

def decodeWord(morseCode):
    return ''.join(MORSE_CODE[letter] for letter in morseCode.split(" "))

print("Trying to decode 'HEY JUDE' - from morse")
decodedMorse = decodeMorse('.... . -.--   .--- ..- -.. .')
print("Decoded Morse: " + decodedMorse)

print("Trying to decode 'HEY JUDE' (TU: 2)- from bits")
decodedBits = decodeBits('1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011')
print("Decoded bits: " + decodedBits + " - Must be:  .... . -.--   .--- ..- -.. .")
decodedMorse = decodeMorse(decodedBits)
print("Decoded Morse: " + decodedMorse)

print("Trying to decode 'Hey JUDE' (TU: 1) - from bits")
decodedBits = decodeBits('10101010001000111010111011100000001011101110111000101011100011101010001')
print("Decoded bits: " + decodedBits + " - Must be:  .... . -.--   .--- ..- -.. .")
decodedMorse = decodeMorse(decodedBits)
print("Decoded Morse: " + decodedMorse)

print("Trying to decode 'Hey JUDE' (TU: 4) - from bits")
decodedBits = decodeBits('11110000111100001111000011110000000000001111000000000000111111111111000011110000111111111111000011111111111100000000000000000000000000001111000011111111111100001111111111110000111111111111000000000000111100001111000011111111111100000000000011111111111100001111000011110000000000001111')
print("Decoded bits: " + decodedBits + " - Must be:  .... . -.--   .--- ..- -.. .")
decodedMorse = decodeMorse(decodedBits)
print("Decoded Morse: " + decodedMorse)

print("Trying to decode 'E' (TU: 1) - from bits")
decodedBits = decodeBits('1')
print("Decoded bits: " + decodedBits + " - Must be: .")
decodedMorse = decodeMorse(decodedBits)
print("Decoded Morse: " + decodedMorse)

print("Trying to decode 'E' (TU: 1) - from bits with noise zeros")
decodedBits = decodeBits('001')
print("Decoded bits: " + decodedBits + " - Must be: .")
decodedMorse = decodeMorse(decodedBits)
print("Decoded Morse: " + decodedMorse)


print("Trying to decode 'M' (TU: 1) - from bits")
decodedBits = decodeBits('1110111')
print("Decoded bits: " + decodedBits + " - Must be: --")
decodedMorse = decodeMorse(decodedBits)
print("Decoded Morse: " + decodedMorse)

print("Trying to decode 'I' (TU: 3) - from bits")
decodedBits = decodeBits('111000111')
print("Decoded bits: " + decodedBits + " - Must be: ..")
decodedMorse = decodeMorse(decodedBits)
print("Decoded Morse: " + decodedMorse)

print("Trying to decode 'T T' (TU: 1) - from bits")
decodedBits = decodeBits('1110000000111')
print("Decoded bits: " + decodedBits + " - Must be: - -")
decodedMorse = decodeMorse(decodedBits)
print("Decoded Morse: " + decodedMorse)

print("Trying to decode 'E' (TU: 3) - from bits ")
decodedBits = decodeBits('111')
print("Decoded bits: " + decodedBits + " - Must be: .")
decodedMorse = decodeMorse(decodedBits)
print("Decoded Morse: " + decodedMorse)

print("Trying to decode '??' (TU: ??) - from bits ")
decodedBits = decodeBits("11111111111111100000000000000011111000001111100000111110000011111000000000000000111110000000000000000000000000000000000011111111111111100000111111111111111000001111100000111111111111111000000000000000111110000011111000001111111111111110000000000000001111100000111110000000000000001111111111111110000011111000001111111111111110000011111000000000000000111111111111111000001111100000111111111111111000000000000000000000000000000000001111111111111110000011111000001111100000111110000000000000001111100000111111111111111000001111100000000000000011111111111111100000111111111111111000001111111111111110000000000000001111100000111111111111111000001111111111111110000000000000001111111111111110000011111000000000000000000000000000000000001111100000111110000011111111111111100000111110000000000000001111111111111110000011111111111111100000111111111111111000000000000000111111111111111000001111100000111110000011111111111111100000000000000000000000000000000000111110000011111111111111100000111111111111111000001111111111111110000000000000001111100000111110000011111111111111100000000000000011111111111111100000111111111111111000000000000000111110000011111111111111100000111111111111111000001111100000000000000011111000001111100000111110000000000000000000000000000000000011111111111111100000111111111111111000001111111111111110000000000000001111100000111110000011111000001111111111111110000000000000001111100000000000000011111000001111111111111110000011111000000000000000000000000000000000001111111111111110000000000000001111100000111110000011111000001111100000000000000011111000000000000000000000000000000000001111100000111111111111111000001111100000111110000000000000001111100000111111111111111000000000000000111111111111111000001111111111111110000011111000001111100000000000000011111111111111100000111110000011111111111111100000111111111111111000000000000000000000000000000000001111111111111110000011111000001111100000000000000011111111111111100000111111111111111000001111111111111110000000000000001111111111111110000011111111111111100000111110000000000000001111100000111111111111111000001111100000111111111111111000001111100000111111111111111")
print("Decoded bits: " + decodedBits + " - Must be: ???")
decodedMorse = decodeMorse(decodedBits)
print("Decoded Morse: " + decodedMorse)
