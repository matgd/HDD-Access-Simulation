MIN = 1
MAX = int(input("Write 'MAX' size of HDD: "))
TIME_PER_BLOCK = float(input("Write 'TIME_PER_BLOCK': "))
HEAD_START = int(input("Write 'HEAD_START' position: "))
DATA_PROCESS_TIME =  float(input("Write 'DATA_PROCESS_TIME': "))
CALLOUTS_FILE = open("callouts.txt")

print()

def FCFS(timePerBlock, head, cFile, dataProcessTime):
    totalCourse = 0
    totalTime = 0
    cFile.seek(0)
    line = cFile.readline()
    while line != "" :
        totalTime += dataProcessTime
        absoluteValue = abs(int(line) - int(head))
        totalCourse += absoluteValue
        totalTime += timePerBlock * absoluteValue
        head = line
        line = cFile.readline()
    print("==== FCFS - Results ====")
    print("Total course: ",totalCourse)
    print("Total time:   ",round(totalTime, 2))
    print()

def SSTF(timePerBlock, head, cFile, dataProcessTime):
    totalCourse = 0
    totalTime = 0
    calloutListPositive = []
    calloutListNegative = []
    cFile.seek(0)
    line = cFile.readline()
    while line != "" :
        totalTime += dataProcessTime
        value = int(line) - int(head)
        if value >= 0:
            calloutListPositive.append(value)
        else:
            calloutListNegative.append(value)
        line = cFile.readline()
    calloutListPositive.sort()
    calloutListNegative.sort()    
    # print(calloutListPositive)
    # print(calloutListNegative)
    while calloutListPositive and calloutListNegative:
        if calloutListPositive[0] <= abs(calloutListNegative[-1]) :
            value = calloutListPositive[0]
            totalCourse += value
            totalTime += timePerBlock * value
            head += calloutListPositive[0]
            calloutListPositive.pop(0)
            calloutListPositive = [x - value for x in calloutListPositive]
            calloutListNegative = [x - value for x in calloutListNegative]
            # print(calloutListPositive)
            # print(calloutListNegative)
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
            # print(calloutListPositive)
            # print(calloutListNegative)
            calloutListPositive.sort()
            calloutListNegative.sort()         
    while calloutListPositive and not calloutListNegative:
        value = calloutListPositive[0]
        totalCourse += value
        totalTime += timePerBlock * value
        head += calloutListPositive[0]
        calloutListPositive.pop(0)
        calloutListPositive = [x - value for x in calloutListPositive]
        # print(calloutListPositive)
    while not calloutListPositive and calloutListNegative:
        value = abs(calloutListNegative[-1])
        totalCourse += value
        totalTime += timePerBlock * value
        head += calloutListNegative[-1]
        calloutListNegative.pop(-1)
        calloutListNegative = [x + value for x in calloutListNegative]
        # print(calloutListNegative)

    print("==== SSTF - Results ====")
    print("Total course: ",totalCourse)
    print("Total time:   ",round(totalTime, 2))
    print()

def SCAN(timePerBlock, head, cFile, dataProcessTime):
    totalCourse = 0
    totalTime = 0
    listLeft = []
    listRight = []
    cFile.seek(0)
    line = cFile.readline()
    while line != "" :
        totalTime += dataProcessTime
        value = int(line)
        if value <= head:
            listLeft.append(value)
        else:
            listRight.append(value)
        line = cFile.readline()
    listLeft.sort()
    listRight.sort()    
    # print(listLeft)
    # print(listRight)
    listLeftAbs = [head - x for x in listLeft]
    listRightAbs = [x - head for x in listRight]
    # print(listLeftAbs)
    # print(listRightAbs)
    if listLeft and not listRight:
        totalCourse += head - MIN
        totalTime += timePerBlock * (head - MIN)
    elif not listLeft and listRight:
        totalCourse += MAX - head
        totalTime += timePerBlock * (MAX - head)
    elif listLeftAbs[-1] <= listRightAbs[0]:
        totalCourse += head - MIN
        totalCourse += MAX - MIN
        totalTime += (head + MAX - MIN - MIN) * timePerBlock
    elif listLeftAbs[-1] > listRightAbs[0]:
        totalCourse += MAX - head
        totalCourse += MAX - MIN
        totalTime += (MAX + MAX - head - MIN) * timePerBlock
    
    print("==== SCAN - Results ====")
    print("Total course: ",totalCourse)
    print("Total time:   ",round(totalTime, 2))
    print()

def CSCAN(timePerBlock, head, cFile, dataProcessTime):
    totalCourse = 0
    totalTime = 0
    listLeft = []
    listRight = []
    cFile.seek(0)
    line = cFile.readline()
    while line != "" :
        totalTime += dataProcessTime
        value = int(line)
        if value <= head:
            listLeft.append(value)
        else:
            listRight.append(value)
        line = cFile.readline()
    listLeft.sort()
    listRight.sort()    
    # print(listLeft)
    # print(listRight)
    listLeftAbs = [head - x for x in listLeft]
    listRightAbs = [x - head for x in listRight]
    # print(listLeftAbs)
    # print(listRightAbs)
    if listLeft and not listRight:
        totalCourse += head - MIN
        totalTime += timePerBlock * (head - MIN)
    elif not listLeft and listRight:
        totalCourse += MAX - head
        totalTime += timePerBlock * (MAX - head)
    else:
        # always goes from right to left
        totalCourse += head - MIN
        totalCourse += MAX - MIN
        totalCourse += MAX - listRight[0]
        totalTime += (head + MAX + MAX - MIN - MIN - listRight[0]) * timePerBlock
    
    print("==== C-SCAN - Results ====")
    print("Total course: ",totalCourse)
    print("Total time:   ",round(totalTime, 2))
    print()

def LOOK(timePerBlock, head, cFile, dataProcessTime):
    totalCourse = 0
    totalTime = 0
    listLeft = []
    listRight = []
    cFile.seek(0)
    line = cFile.readline()
    while line != "" :
        totalTime += dataProcessTime
        value = int(line)
        if value <= head:
            listLeft.append(value)
        else:
            listRight.append(value)
        line = cFile.readline()
    listLeft.sort()
    listRight.sort()    
    # print(listLeft)
    # print(listRight)
    listLeftAbs = [head - x for x in listLeft]
    listRightAbs = [x - head for x in listRight]
    # print(listLeftAbs)
    # print(listRightAbs)
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
    print("Total course: ",totalCourse)
    print("Total time:   ",round(totalTime, 2))
    print()

def CLOOK(timePerBlock, head, cFile, dataProcessTime):
    totalCourse = 0
    totalTime = 0
    listLeft = []
    listRight = []
    cFile.seek(0)
    line = cFile.readline()
    while line != "" :
        totalTime += dataProcessTime
        value = int(line)
        if value <= head:
            listLeft.append(value)
        else:
            listRight.append(value)
        line = cFile.readline()
    listLeft.sort()
    listRight.sort()    
    # print(listLeft)
    # print(listRight)
    listLeftAbs = [head - x for x in listLeft]
    listRightAbs = [x - head for x in listRight]
    # print(listLeftAbs)
    # print(listRightAbs)
    if listLeft and not listRight:
        totalCourse += head - listLeft[0]
        totalTime += timePerBlock * (head - listLeft[0])
    elif not listLeft and listRight:
        totalCourse += listRight[-1] - head
        totalTime += timePerBlock * (listRight[-1] - head)
    else:
        # always goes from right to left
        totalCourse += head - listLeft[0]
        totalCourse += listRight[-1] - listLeft[0]
        totalCourse += listRight[-1] - listRight[0]
        totalTime += (head + listRight[-1] + listRight[-1] - listLeft[0] - listRight[0] - listLeft[0]) * timePerBlock
    
    print("==== C-LOOK - Results ====")
    print("Total course: ",totalCourse)
    print("Total time:   ",round(totalTime, 2))
    print()    
    
FCFS(TIME_PER_BLOCK, HEAD_START, CALLOUTS_FILE, DATA_PROCESS_TIME)
SSTF(TIME_PER_BLOCK, HEAD_START, CALLOUTS_FILE, DATA_PROCESS_TIME)
SCAN(TIME_PER_BLOCK, HEAD_START, CALLOUTS_FILE, DATA_PROCESS_TIME)
CSCAN(TIME_PER_BLOCK, HEAD_START, CALLOUTS_FILE, DATA_PROCESS_TIME)
LOOK(TIME_PER_BLOCK, HEAD_START, CALLOUTS_FILE, DATA_PROCESS_TIME)
CLOOK(TIME_PER_BLOCK, HEAD_START, CALLOUTS_FILE, DATA_PROCESS_TIME)
CALLOUTS_FILE.close()
input() # for console in order to read results
