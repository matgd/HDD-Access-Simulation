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

    [head - x for x in listLeft]
    [x - head for x in listRight]

    if listLeft and not listRight:
        totalCourse += head - minSize
        totalTime += timePerBlock * (head - minSize)
    elif not listLeft and listRight:
        totalCourse += maxSize - head
        totalTime += timePerBlock * (maxSize - head)
    else:
        totalCourse += head - minSize
        totalCourse += maxSize - minSize
        totalCourse += maxSize - listRight[0]
        totalTime += (head + maxSize + maxSize - minSize - minSize - listRight[0]) * timePerBlock

    print("==== C-SCAN - Results ====")
    print("Total course: ", totalCourse)
    print("Total time:   ", round(totalTime, 2))
    print("\n")
