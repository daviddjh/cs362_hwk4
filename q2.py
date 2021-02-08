
def calcAvgValue(dlist):
    if type(dlist) != list:
        raise TypeError("need a list")

    if len(dlist) == 0:
        raise ValueError("cant have an empty list")
    
    avgValue = 0.0
    for value in dlist:
        if type(value) != int and type(value) != float:
            raise ValueError("Only List of Numbers Allowed")
        avgValue += value
    avgValue = avgValue / len(dlist)
    return avgValue