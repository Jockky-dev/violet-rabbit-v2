---
layout: post
title: coded while drunk ~admin
description: coded while drunk ~admin
summary: what tf is this python
tags: Python
minute: 1
---

```python
# Puzzle 2
def encrypt(s1):
    s2 = map(lambda c : chr(ord(c) + 2), s1)
    return ''.join(s2)


def decrypt(s1):
    s2 = map(lambda c : chr(ord(c) - 2), s1)
    return ''.join(s2)


s = "xtherussiansarecomingx"
print(decrypt(encrypt(encrypt(s)))==encrypt(s))
```