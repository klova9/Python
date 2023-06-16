#Return True if the string "cat" and "dog" appear the same number of times in the given string.

def cat_dog(string):
    if string.find('cat') != -1 and string.find('dog') != -1:
        print('True')
    else:
        print('false')
cat_dog('catdog')# → True
cat_dog('catcat')# → False
cat_dog('1cat1cadodog')# → True