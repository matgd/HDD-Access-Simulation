def execute(maxSize, minSize, timePerBlock, head, calloutsFile, dataProcessTime):
    totalCourse = 0
    totalTime = 0
    listLeft = []
    listRight = []
    calloutsFile.seek(0)

    for line in calloutsFile:
        totalTime += dataProcessTime
        value = int(line)
        if value <= head:
            listLeft.append(value)
        else:
            listRight.append(value)

    listLeft.sort()
    listRight.sort()

    listLeftAbs = [head - x for x in listLeft]
    listRightAbs = [x - head for x in listRight]

    if listLeft and not listRight:
        totalCourse += head - minSize
        totalTime += timePerBlock * (head - minSize)
    elif not listLeft and listRight:
        totalCourse += maxSize - head
        totalTime += timePerBlock * (maxSize - head)
    elif listLeftAbs[-1] <= listRightAbs[0]:
        totalCourse += head - minSize
        totalCourse += maxSize - minSize
        totalTime += (head + maxSize - minSize - minSize) * timePerBlock
    elif listLeftAbs[-1] > listRightAbs[0]:
        totalCourse += maxSize - head
        totalCourse += maxSize - minSize
        totalTime += (maxSize + maxSize - head - minSize) * timePerBlock

    print("==== SCAN - Results ====")
    print("Total course: ", totalCourse)
    print("Total time:   ", round(totalTime, 2))
    print("\n")
