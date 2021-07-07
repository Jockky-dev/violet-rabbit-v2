---
layout: post
title: what's this code, fastest one wins :) 
description: What's this file 
summary: What's this file
tags: 
minute: 1
---

```
<!DOCTYPE html>
<html>
<head>
    <title>Flag!Flag!Flag!</title>
    <link rel="stylesheet" href="css/main.css">
</head>
<body>
    <div class='contain-flag'>
      <div class='pole'></div>
      <div class='flag'></div>
      <div class='shadow'></div>
      <div class='flag flag-2'></div>
    </div>
    <div>
        <center>
        <h3>This is just a decoy of the FLAG!</h3>
        <small>If you ask nicely, maybe i will give it to you.</small>
        <small>View Source of this page <a href="https://pankace.github.io/magenta-cat-3743/" target="_blank">Here</a></small>
        </center>
    </div>
    <pre><?php
    $flag = #REDACTED
    if(array_key_exists("flag", $_GET)) {
        if({{ site.flag.flag }}=== "true"){
        echo $flag;
        }
    }
    ?>
    </pre>
```