def execute(timePerBlock, head, calloutsFile, dataProcessTime):
    totalCourse = 0
    totalTime = 0
    calloutsFile.seek(0)

    for line in calloutsFile:
        totalTime += dataProcessTime
        absoluteValue = abs(int(line) - int(head))
        totalCourse += absoluteValue
        totalTime += timePerBlock * absoluteValue
        head = line

    print("==== FCFS - Results ====")
    print("Total course: ",totalCourse)
    print("Total time:   ",round(totalTime, 2))
    print("\n")