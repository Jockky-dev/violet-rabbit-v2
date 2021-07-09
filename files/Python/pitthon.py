#author https://github.com/ImSoZRious

charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+[]{}/\\|"

def charadd(c, x):
    return charset[ ( charset.find(c) + x ) % len(charset) ]

s = "Stupid_Hackathon_Thailand" 
key = int(input())

offset = [31, 4, 23, 32, 27, 27, 40, 42, 59, 62, 19, 42, 49, 26, 69, 37, 54, 55, 47, 60, 54, 26, 20, 40, 63]

output = ""

for i in range(len(s)):
  new_char = charadd(s[i], (key * ( i ** key )) + (key ** 2)  +  (offset[i]))
  output += new_char

print(output)