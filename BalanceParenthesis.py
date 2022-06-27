def testArray(array, startIndex, currentIndex):
    if len(array) == startIndex and currentIndex == 0:
        return "Balanced Parenthesis"
    elif len(array) == startIndex and currentIndex != 0:
        return "Un Balanced Parenthesis"
    elif currentIndex < 0:
        return "Un Balanced Parenthesis"
    elif array[startIndex] == '(':
        return testArray(array, startIndex + 1, currentIndex + 1)
    elif array[startIndex] == ')':
        return testArray(array, startIndex + 1, currentIndex - 1)
    else:
        return testArray(array,startIndex + 1, currentIndex)


array = [i for i in input()]
print(testArray(array, 0, 0))
