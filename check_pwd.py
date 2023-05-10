# PWD function
# some code adapted from "Exploration: Random Testing"
def check_pwd(input):
    if len(input) == 0:
        return False
    if len(input) < 8:
        return False
    if len(input) > 20:
        return False
    if not any(char.islower() for char in input):
        return False
    if not any(char.isupper() for char in input):
        return False
    if not any(char.isdigit() for char in input):
        return False

    return True
