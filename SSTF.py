def execute(timePerBlock, head, calloutsFile, dataProcessTime):
    totalCourse = 0
    totalTime = 0
    calloutListPositive = []
    calloutListNegative = []
    calloutsFile.seek(0)

    for line in calloutsFile:
        totalTime += dataProcessTime
        value = int(line) - int(head)
        if value >= 0:
            calloutListPositive.append(value)
        else:
            calloutListNegative.append(value)

    calloutListPositive.sort()
    calloutListNegative.sort()

    while calloutListPositive and calloutListNegative:
        if calloutListPositive[0] <= abs(calloutListNegative[-1]) :
            value = calloutListPositive[0]
            totalCourse += value
            totalTime += timePerBlock * value
            head += calloutListPositive[0]
            calloutListPositive.pop(0)
            calloutListPositive = [x - value for x in calloutListPositive]
            calloutListNegative = [x - value for x in calloutListNegative]
            calloutListPositive.sort()
            calloutListNegative.sort()
        else:
            value = abs(calloutListNegative[-1])
            totalCourse += value
            totalTime += timePerBlock * (value)
            head += calloutListNegative[-1]
            calloutListNegative.pop(-1)
            calloutListPositive = [x + value for x in calloutListPositive]
            calloutListNegative =[x + value for x in calloutListNegative]
            calloutListPositive.sort()
            calloutListNegative.sort()

    while calloutListPositive and not calloutListNegative:
        value = calloutListPositive[0]
        totalCourse += value
        totalTime += timePerBlock * value
        head += calloutListPositive[0]
        calloutListPositive.pop(0)
        calloutListPositive = [x - value for x in calloutListPositive]

    while not calloutListPositive and calloutListNegative:
        value = abs(calloutListNegative[-1])
        totalCourse += value
        totalTime += timePerBlock * value
        head += calloutListNegative[-1]
        calloutListNegative.pop(-1)
        calloutListNegative = [x + value for x in calloutListNegative]

    print("==== SSTF - Results ====")
    print("Total course: ",totalCourse)
    print("Total time:   ",round(totalTime, 2))
    print("\n")