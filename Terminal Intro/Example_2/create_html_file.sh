#!/bin/sh

# Declare variables
filename=html_file.html
html_content="<!DOCTYPE html>
<html>
<head>
<meta charset=\"utf-8\" />
<title>Sample HTML file</title>

</head>

<style>
    body {
        font-family: monospace;
    }
</style>

<body>
<h1>It works!</h1>
</body>
</html>"

# Echo content of variable into file
echo $html_content > $filename