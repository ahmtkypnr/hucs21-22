email = input("Enter your e-mail address: ")
def is_valid(email):
    if("@" and "." in email):
        return True
    return False
if(is_valid(email)):
    print("This is a valid e-mail address")
else:
    print("This isn't a valid e-mail address")