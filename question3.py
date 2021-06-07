def findPair(array, target):
    print("Target:", target, " Array: ", array)

    checkedSet = set()

    for i in range(0, len(array)):
        temp = target - array[i]
        if(temp in checkedSet):
            print("Pair: ", str(array[i]), ", ", str(temp))
        checkedSet.add(array[i])
    
arr = [1, 3, 4, 5]
val = 7

findPair(arr, val)