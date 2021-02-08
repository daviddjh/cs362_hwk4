
def computeVolume(length):
    if (type(length) == int or type(length) == float):
        return length * length * length
    else:
        raise TypeError("Only Numbers Allowed")
