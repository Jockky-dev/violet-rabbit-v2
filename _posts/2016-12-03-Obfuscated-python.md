---
layout: post
title: coded while drunk ~admin
description: coded while drunk ~admin
summary: what tf is this, this enigma ?
tags: Python
minute: 1
---


challenges has already been completed<br>

<img src="https://raw.githubusercontent.com/pankace/violet-rabbit-v2/master/problems.jpg?token=AKUHUPTLZMOG2NEMZ4KVU4DA6DXYA" alt="done">

challenges has already been completed<br>

```
#author https://github.com/ImSoZRious
``` 
<br>
what tf is this, this enigma?
So I was at the bar the other day ..... uh i forgot shit 
uhhhh wtf


oh files <br>

```python 

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
```

<br>
[python?](https://pankace.github.io/violet-rabbit-v2/files/Python/pitthon.py)<br>
[since this is too hard here is the key](https://pankace.github.io/violet-rabbit-v2/files/Python/drunk.py)
