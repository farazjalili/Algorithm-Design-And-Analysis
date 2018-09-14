
def BinarySearch(_array,_item):
    firstOfArray=0
    lastOfArray=len(_array)
    found = False
    while firstOfArray <= lastOfArray and not found :
        midpointOfArray = (firstOfArray + lastOfArray)//2
        if _array[midpointOfArray] ==_item :
            found=True
        else  :
            if _item < _array[midpointOfArray] :
                lastOfArray = midpointOfArray -1
            else :
                firstOfArray = midpointOfArray +1
    return found




if __name__=="__main__":
    array = [7,10,20,21,23,29,30,56,32]
    print(BinarySearch(array,7))