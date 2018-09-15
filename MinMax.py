
def MaxFinder(_array):
    if(len(_array)<2):
        return _array
    midOfArray=len(_array)/2
    left=MaxFinder(_array[:midOfArray])
    right=MaxFinder(_array[midOfArray:])
    result=max(left,right)
    return result
def MinFinder(_array):
    if(len(_array)<2):
        return _array
    midOfArray=len(_array)/2
    left=MinFinder(_array[:midOfArray])
    right=MinFinder(_array[midOfArray:])
    result=min(left,right)
    return result

if __name__=="__main__":
    sample=[9,12,1,6,29,12,96,12]
    x=MaxFinder(sample)
    y=MinFinder(sample)
    print x,y
    