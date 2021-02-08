
def fullName(firstname, lastname):
    if type(firstname) != str or type(lastname) != str:
        raise(TypeError)
    else:
        return firstname + " " + lastname
    