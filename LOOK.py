def execute(timePerBlock, head, calloutsFile, dataProcessTime):
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
        totalCourse += head - listLeft[0]
        totalTime += timePerBlock * (head - listLeft[0])
    elif not listLeft and listRight:
        totalCourse += listRight[-1] - head
        totalTime += timePerBlock * (listRight[-1] - head)
    elif listLeftAbs[-1] <= listRightAbs[0]:
        totalCourse += head - listLeft[0]
        totalCourse += listRight[-1] - listLeft[0]
        totalTime += (head + listRight[-1] - listLeft[0] - listLeft[0]) * timePerBlock
    elif listLeftAbs[-1] > listRightAbs[0]:
        totalCourse += listRight[-1] - head
        totalCourse += listRight[-1] - listLeft[0]
        totalTime += (listRight[-1] + listRight[-1] - head - listLeft[0]) * timePerBlock

    print("==== LOOK - Results ====")
    print("Total course: ", totalCourse)
    print("Total time:   ", round(totalTime, 2))
    print("\n")