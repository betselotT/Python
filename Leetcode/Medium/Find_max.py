def findMaxOnes(userInput):
    counterArr = []
    if 0 not in userInput:
        return userInput.count(1)
    else:
        counter = 0
        zeroCounter = 0
        for i in range(len(userInput)):
            if userInput[i] == 1:
                counter = counter + 1
                if zeroCounter > 1:
                    counterArr.extend([0] * zeroCounter - 1)
                zeroCounter = 0
            elif userInput[i] == 0:
                counterArr.append(counter)
                zeroCounter = zeroCounter + 1
                counter = 0
        counterArr.append(counter)
        sumArr = []
        for i in range(1, len(counterArr)):
            sumArr.append(counterArr[i] + counterArr[i-1])
        return max(sumArr) + 1

print(findMaxOnes([1,0,0,1,1,0,0,1,1]))