
class Queue:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.insert(0, item)
    
    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)


print("Enter the number of process:")
n = int(input())

print("Enter the Quantum Time:")
quantum = int(input())
processes = []
processComplete = []
completetionTime = []
burstTime = []
burstTime1 = []
arrivalTime = []
turnAroundTime = []
waitingTime = []
proceeInQueue = []
for i in range(0, n):
    processes.insert(i, i + 1)
    processComplete.insert(i, 0)
    completetionTime.insert(i, 0)
    turnAroundTime.insert(i,0)
    waitingTime.insert(i, 0)
    proceeInQueue.insert(i,0)
for i in range(0, n):
    burstTime.insert(i, int(raw_input("Enter the burst time of the processes:")))


burstTime1 = burstTime[:]
for i in range(0, n):
    arrivalTime.insert(i, int(raw_input("Enter the Arrival Time of the processes:")))

chartArray = []
processArray = []
chartArray.insert(0, arrivalTime[0])
processArray.insert(0, -1)
sum = arrivalTime[0]
sumIndex = 1

#waitingProcess = []
#waitingProcess.insert(0, processes[0])
count = 0

q = Queue()
q.enqueue(processes[0])
proceeInQueue[0] = 1
while (count < n):
    de = q.dequeue() - 1
    if processComplete[de] != 1:
        if burstTime[de] < quantum:
            sum += burstTime[de]
            burstTime[de] -= burstTime[de]
        else:
            sum += quantum
            burstTime[de] -= quantum
        chartArray.insert(sumIndex, sum)
        sumIndex += 1
        for i in range(0, n):
            if arrivalTime[i] <= sum and proceeInQueue[i] != 1:
                q.enqueue(processes[i])
                proceeInQueue[i] = 1
        if burstTime[de] == 0:
            count += 1
            processComplete[de] = 1
            completetionTime[de] = sum
        else:
            q.enqueue(processes[de])




for i in range(0,n):
    turnAroundTime[i] = completetionTime[i] - arrivalTime[i]
    waitingTime[i] = turnAroundTime[i] - burstTime1[i]

print(chartArray)
print ("Completion Time  :" ,completetionTime)
print("Turn Around Time:  ",turnAroundTime)
print ("Waiting Time:  ",waitingTime)

