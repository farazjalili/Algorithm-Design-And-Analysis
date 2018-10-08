leftList=[]
rightList=[]
def merge_lists(left_sublist,right_sublist):
    i,j = 0,0
    print(left_sublist,right_sublist)
    result = []
    return result
def merge_sort(input_list):
    #if list contains only 1 element return it
    if len(input_list) <= 1:
        return input_list
    else:
        #split the lists into two sublists and recursively split sublists
        midpoint = int(len(input_list)/2)
        leftList.append(input_list[:midpoint])
        left_sublist = merge_sort(input_list[:midpoint])
        right_sublist = merge_sort(input_list[midpoint:])
        rightList.append(input_list[midpoint:])
        #return the merged list using the merge_list function above
        return merge_lists(left_sublist,right_sublist)
number_list = [3,1,5,3,2,5,8,2,9,6,12,53,75,22,83,123,12123]
print(merge_sort(number_list))