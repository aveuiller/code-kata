import math
def sillycase(silly):
    centerIndex = int(math.ceil(len(silly)/2.0))
    return silly[:centerIndex].lower() + silly[centerIndex:].upper()

print(sillycase('foobar'))
print(sillycase('codewars'))
print(sillycase('brian'))
