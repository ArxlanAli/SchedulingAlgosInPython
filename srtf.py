class Queue:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.insert(0,item)
    
    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)


def returnMinimumShortestRemaingTime():
    min = burstTime[waitingProcess[0]-1]
    index = waitingProcess[0]-1
    simpleIndex = 0
    if len(waitingProcess) >= 2:
        for i in range(1,len(waitingProcess)):
            if min > burstTime[waitingProcess[i]-1] and processComplete[waitingProcess[i]-1] != 1:
                min = burstTime[waitingProcess[i]-1]
                index = waitingProcess[i]-1
                simpleIndex = i
            elif min == burstTime[waitingProcess[i]-1] and processComplete[waitingProcess[i]-1] != 1:
                if arrivalTime[index] < arrivalTime[waitingProcess[i]-1]:
                    min = burstTime[index]
                    index = waitingProcess[index] - 1
                    simpleIndex = i
                else:
                    min = burstTime[waitingProcess[i]-1]
                    index = waitingProcess[i] - 1
                    simpleIndex = i
        return index
    else:
        return index


print("Enter the number of process:")
n = int(input())
processes = []
processComplete = []
burstTime = []
arrivalTime = []
for i in range(0,n):
    processes.insert(i,i+1)
    processComplete.insert(i,0)
for i in range(0,n):
    burstTime.insert(i,int(raw_input("Enter the burst time of the processes:")))


for i in range(0,n):
    arrivalTime.insert(i,int(raw_input("Enter the Arrival Time of the processes:")))

chartArray = []
processArray = []
chartArray.insert(0,arrivalTime[0])
processArray.insert(0,-1)
sum = arrivalTime[0]
sumIndex = 1

waitingProcess = []
waitingProcess.insert(0,processes[0])
count = 0
while(count <= n):
    if len(waitingProcess) != n:
        de = returnMinimumShortestRemaingTime()
        print(de)
        if processComplete[de] != 1:
            sum += 1
            chartArray.insert(sumIndex,sum)
            processArray.insert(sumIndex,de+1)
            sumIndex +=1
            burstTime[de] -= 1
            for i in range(0,n):
                if arrivalTime[i] == sum:
                    waitingProcess.append(processes[i])
            if burstTime[de] == 0:
                count+=1
                processComplete.insert(de,1)
    else:
        de = returnMinimumShortestRemaingTime()
        print(de)
        if processComplete[de] != 1:
            sum += burstTime[de]
            chartArray.insert(sumIndex,sum)
            processArray.insert(sumIndex,de+1)
            sumIndex +=1
            burstTime[de] = 0
            if burstTime[de] == 0:
                count+=1
                processComplete.insert(de,1)

print(chartArray)
