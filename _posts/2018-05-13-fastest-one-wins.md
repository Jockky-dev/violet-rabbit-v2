---
layout: post
title: what's this code, fastest one wins :) 
description: What's this file 
summary: What's this file
tags: 
minute: 1
---

```
    <pre><?php
    $flag = #REDACTED
 
    if(array_key_exists("flag", $_GET)) {
        if({{ site.data.flag.flag }}=== "true"){
        echo $flag;
        }
    }
    ?>
    </pre>
```