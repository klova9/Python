# Leave only two numbers after the floating point in every number
import re 
sample = """
function foo() {return bar();}
function Foo() {return Bar();}
function Baz(x) {return function(y){return x+y;}}
function bazEx(x) {return function(y, z){return x+y+z;}}
function bar() {return 0;}
function Bar() {return 1;}
"""
search = re.findall(r'[a-z]\w*\s\w*\(\)', sample)
print(search)