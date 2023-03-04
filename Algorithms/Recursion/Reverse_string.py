#Reverse a String using recursion.

def string_rev(string):
    if len(string) > 0:
        string_rev(string[1:])
        print(string[0],end="")
string_rev("I'm Batman")