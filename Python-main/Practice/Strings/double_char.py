#Given a string, return a string where #for every char in the original, there #are two chars.

def double_char(word):
    double_word = ''
    for char in word:
        double_word += char*2
        return double_word
    print(double_word)    

double_char('The')# → 'TThhee'
double_char('AAbb')# → 'AAAAbbbb'
double_char('Hi-There')# → 'HHii--TThheerree'