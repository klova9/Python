# It is a common wisdom that regular expressions are not a good way of dealing with HTML, and there are perfectly good reasons for this. But in this excercise you only need to match simple HTML tags.
import re 
sample = """
<!DOCTYPE html>
<html>
<head>
<title>This is a title</title>
</head>
<body>
<p>Hello world!</p>
</body>
</html>
"""
search = re.findall(r'\<\/*\w*\>', sample)
print(search)