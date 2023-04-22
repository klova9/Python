"""
The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.
"""
def sleep_in(weekday, vacation):
    if weekday == False or vacation == True:
        print("You can sleep in")
    else: 
        print("You can't sleep in")

sleep_in(False, False)
sleep_in(True, False)
sleep_in(False, True)