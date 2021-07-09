#author https://github.com/ImSoZRious
#solve it in bash for extra roles'n shit 
charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+[]{}/\\|"
#solve it in bash for extra roles'n shit 
def charadd(c, x):
    return charset[ ( charset.find(c) + x ) % len(charset) ]
#solve it in bash for extra roles'n shit 
s = "Stupid_Hackathon_Thailand" 
key = int(input())
#solve it in bash for extra roles'n shit 
offset = [31, 4, 23, 32, 27, 27, 40, 42, 59, 62, 19, 42, 49, 26, 69, 37, 54, 55, 47, 60, 54, 26, 20, 40, 63]
#solve it in bash for extra roles'n shit 
output = ""
#solve it in bash for extra roles'n shit 
for i in range(len(s)):
  new_char = charadd(s[i], (key * ( i ** key )) + (key ** 2)  +  (offset[i]))
  output += new_char
#solve it in bash for extra roles'n shit 
print(output)
#solve it in bash for extra roles'n shit 
