# PWD function
def check_pwd(input):
    if len(input) == 0:
        return False

    if len(input) < 8:
        return False

    if len(input) > 20:
        return False

    return True
