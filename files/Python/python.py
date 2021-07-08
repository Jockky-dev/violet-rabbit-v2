## Puzzle 2
#def encrypt(s1):
#    s2 = map(lambda c : chr(ord(c) + 2), s1)
#    return ''.join(s2)
#def decrypt(s1):
#    s2 = map(lambda c : chr(ord(c) - 2), s1)
#    return ''.join(s2)
#s = "LAZY-MINATO-AQUA"
#print(decrypt(encrypt(encrypt(s)))==encrypt(s))
#
#
def convert_to_ascii(text):
    return ",".join(str(ord(char)) for char in text)

data = (LAZY-MINATO-AQUA)

convert_to_ascii(data)
values = [int(i) for i in x.split(',')] 
array = np.array(values)