import FCFS, SSTF, SCAN, CSCAN, LOOK, CLOOK

MIN = 1
MAX = int(input("Write 'MAX' size of HDD: "))
TIME_PER_BLOCK = float(input("Write 'TIME_PER_BLOCK': "))
HEAD_START = int(input("Write 'HEAD_START' position: "))
DATA_PROCESS_TIME =  float(input("Write 'DATA_PROCESS_TIME': "))
print("\n")

with open("callouts.txt") as CALLOUTS_FILE:
    FCFS.execute(TIME_PER_BLOCK, HEAD_START, CALLOUTS_FILE, DATA_PROCESS_TIME)
    SSTF.execute(TIME_PER_BLOCK, HEAD_START, CALLOUTS_FILE, DATA_PROCESS_TIME)
    SCAN.execute(MAX, MIN, TIME_PER_BLOCK, HEAD_START, CALLOUTS_FILE, DATA_PROCESS_TIME)
    CSCAN.execute(MAX, MIN, TIME_PER_BLOCK, HEAD_START, CALLOUTS_FILE, DATA_PROCESS_TIME)
    LOOK.execute(TIME_PER_BLOCK, HEAD_START, CALLOUTS_FILE, DATA_PROCESS_TIME)
    CLOOK.execute(TIME_PER_BLOCK, HEAD_START, CALLOUTS_FILE, DATA_PROCESS_TIME)

input("\n") # for console (in Windows OS) in order to read results
