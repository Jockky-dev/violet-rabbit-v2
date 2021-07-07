---
layout: post
title: what's this code, fastest one wins :) 
description: What's this file 
summary: What's this file
tags: 
minute: 1
---


<!DOCTYPE Html />
<html>
 <head>
 <meta charset="utf-8">
 <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
 <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
 <style type="text/css">
 .ins {
  padding:auto;
  margin:5rem auto 0 auto;
  text-align:center;
 }
 .btn {
  padding:auto;
  margin:1rem;
 }
 </style>
 <title>Rot Player</title>
 </head>
 <body>
<div class="container text-center">
 <h2>Rot Player</h2><small>Entry Point</small>
 <div class="container ins">
	 <input type="text" name="flag" id="flag" placeholder="Enter the flag" /><br>
	 <button class="btn btn-primary" id="check" >Login with Flag!</button>
 </div>
</div>

 <script type="text/javascript">
 document.getElementById("check").onclick = function () {
 var flag = document.getElementById("flag").value;
 var rotFlag = flag.replace(/[a-zA-Z]/g, function(c){
 return String.fromCharCode((c <= "Z" ? 90 : 122) >= (c = c.charCodeAt(0) + 13) ? c : c - 26);});
 if ("TYHT{py13a7_51q3_y061a_j17u_e0713!}" == rotFlag) {
 alert("Correct flag!");
 } else {
 alert("Incorrect flag, rot again");
 }
 }
 </script>

 </body>
</html>