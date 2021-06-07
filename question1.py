def reverseString(input):
    splitString = input.split(' ')
    output = ""

    for i in range(len(splitString)):
        output += (splitString[len(splitString) - i - 1])
        if (i != len(splitString) - 1):
            output += " "

    return output
