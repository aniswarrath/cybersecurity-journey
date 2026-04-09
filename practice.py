def check_username (username) :
    if len(username) < 3 :
        return "Too short"
    elif len(username) > 15 :
        return "Too long"
    else :
        return "valid"
    
username = (input("Enter a username: "))
print(check_username(username))