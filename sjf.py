def returnFirstOrder():
    for i in range(0,len(burstTime)):
        if processComplete[i] != 1:
            return i

def returnIndexOfLoweseBurst():
    min = returnFirstOrder()
    for i in range(returnFirstOrder() + 1,len(burstTime)):
        if burstTime[i] < burstTime[min] and processComplete[i] != 1:
            min = i
    processComplete[min] = 1
    return min


print("Enter the number of process:")
n = int(input())
processes = []
processComplete = []
burstTime = []
order = []
arrivalTime = []
for i in range(0,n):
    processes.insert(i,i+1)
    processComplete.insert(i,0)
for i in range(0,n):
    burstTime.insert(i,int(raw_input("Enter the burst time of the processes:")))


for i in range(0,n):
    arrivalTime.insert(i,int(raw_input("Enter the Arrival Time of the processes:")))


sum = 0
waiting = []
runningProcess = []
turnAround = []
waiting.insert(0,0)
for i in range(0,n):
    proces = returnIndexOfLoweseBurst()
    runningProcess.insert(i,proces+1)
    sum += burstTime[proces]
    waiting.insert(i+1,sum)
    turnAround.insert(i,sum-arrivalTime[i])


print(waiting)
print(turnAround)
sum1 = 0.0
sum2 = 0.0
for i in range(0,len(waiting) - 1):
    sum1 += waiting[i] - arrivalTime[i]
    sum2 += turnAround[i]
    print("Waiting time of Process" + str(runningProcess[i]) + " is  "+ str(waiting[i] - arrivalTime[i]))
    print("Arrival time of Process" + str(runningProcess[i]) + " is  "+ str(turnAround[i]))

print("Average Waiting Time is " + str(float(float(sum1) / n)))
print("Average TurnAround Time is " + str(float(float(sum2) / n)))



