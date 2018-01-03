def returnFirstMin():
    for i in range(0,len(priority)):
        if processComplete[i] != 1:
            return i

def returnIndexOfHighestPriority():
    min = returnFirstMin()
    for i in range(returnFirstMin() + 1,len(priority)):
        if priority[i] < priority[min] and processComplete[i] != 1:
            min = i
    processComplete[min] = 1
    return min


print("Enter the number of process:")
n = int(input())
processes = []
processComplete = []
burstTime = []
priority = []
for i in range(0,n):
    processes.insert(i,i+1)
    processComplete.insert(i,0)
for i in range(0,n):
    burstTime.insert(i,int(raw_input("Enter the burst time of the processes:")))

for i in range(0,n):
    priority.insert(i,int(raw_input("Enter the Priority of the processes:")))


sum = 0
waiting = []
waitingProcess = []
waiting.insert(0,0)
for i in range(0,n):
    proces = returnIndexOfHighestPriority()
    waitingProcess.insert(i,proces+1)
    sum += burstTime[proces]
    waiting.insert(i+1,sum)

sum1 = 0.0
for i in range(0,len(waiting) - 1):
    sum1 += waiting[i]
    print("Waiting time of Process" + str(waitingProcess[i]) + " is  "+ str(waiting[i]))

print("Average Waiting Time is " + str(float(float(sum1) / n)))


